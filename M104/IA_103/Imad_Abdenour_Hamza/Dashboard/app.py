import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import norm

# CONFIG
st.set_page_config(page_title="Dashboard Abonnements", layout="wide")

# LOAD DATA
@st.cache_data
def load_data():
    df = pd.read_csv("data.csv")
    df['created_date'] = pd.to_datetime(df['created_date'], errors='coerce')
    df['canceled_date'] = pd.to_datetime(df['canceled_date'], errors='coerce')
    df['duration_days'] = (df['canceled_date'] - df['created_date']).dt.days
    return df

data = load_data()

#1 Affichage des premières lignes du DataFrame pour avoir un aperçu des données.
print("\nTypes de colonnes :")

#2 Vérification des valeurs manquantes dans chaque colonne.
data['canceled_date'] = data['canceled_date'].fillna('Active')
# 3. Détection des incohérences
data.drop_duplicates()

# SIDEBAR
st.sidebar.title("🔎 Filtres")

paid_filter = st.sidebar.selectbox(
    "Abonnement payé",
    ["Tous", "Yes", "No"]
)

date_range = st.sidebar.date_input(
    "Filtrer par date",
    [data['created_date'].min(), data['created_date'].max()]
)

# Application des filtres
if paid_filter != "Tous":
    data = data[data['was_subscription_paid'] == paid_filter]

if len(date_range) == 2:
    data = data[
        (data['created_date'] >= pd.to_datetime(date_range[0])) &
        (data['created_date'] <= pd.to_datetime(date_range[1]))
    ]

# TITLE
st.title("📊 Dashboard des Abonnements")

# KPIs
st.subheader("📈 Indicateurs clés")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Durée moyenne", round(data['duration_days'].mean(), 2))
col2.metric("Durée médiane", round(data['duration_days'].median(), 2))
col3.metric("Écart-type", round(data['duration_days'].std(), 2))
col4.metric("Taux de churn (%)", round(data['canceled_date'].notna().mean()*100, 2))

# GRAPHIQUES

col1, col2 = st.columns(2)

# Histogramme
with col1:
    st.subheader("📅 Inscriptions par mois")
    monthly = data['created_date'].dt.to_period("M").value_counts().sort_index()

    fig, ax = plt.subplots()
    monthly.plot(kind='bar', ax=ax)
    ax.set_xlabel("Mois")
    ax.set_ylabel("Nombre")
    st.pyplot(fig)

# Boxplot
with col2:
    st.subheader("⏳ Durée des abonnements")
    fig, ax = plt.subplots()
    sns.boxplot(x=data['duration_days'], ax=ax)
    st.pyplot(fig)

st.subheader("💰 Répartition Paiement")

fig, ax = plt.subplots()
data['was_subscription_paid'].value_counts().plot(
    kind='pie',
    autopct='%1.1f%%',
    ax=ax
)
st.pyplot(fig)

st.subheader("📊 Analyse probabiliste")

p_cancel_notpaid = data[data['was_subscription_paid']=="No"]['canceled_date'].notna().mean()

st.write(f"🔹 P(Annulé | Non payé) = {p_cancel_notpaid:.2f}")

mean = data['duration_days'].mean()
std = data['duration_days'].std()

prob_30 = norm.cdf(30, mean, std)

st.write(f"🔹 P(Durée < 30 jours) = {prob_30:.2f}")

st.subheader("📋 Données")
st.dataframe(data)