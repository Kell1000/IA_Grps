Analyse et Dashboard des Abonnements
📄 Description

Ce projet analyse les données d’abonnements pour comprendre :

La durée des abonnements
Le statut de paiement (payé / non payé)
Les annulations (churn)
Les relations entre le coût, la durée et le paiement

Le projet inclut également un dashboard interactif Streamlit pour visualiser ces informations.

🗂️ Contenu du code
1. Prétraitement des données
Import des bibliothèques : pandas, matplotlib, seaborn, scipy, streamlit
Chargement des données depuis data.csv
Gestion des valeurs manquantes dans canceled_date
Conversion des colonnes created_date et canceled_date en datetime
Création d’une nouvelle colonne duration_days pour mesurer la durée des abonnements
Suppression des doublons et détection des incohérences
2. Analyse descriptive
Statistiques sur subscription_cost : moyenne, médiane, écart-type, quartiles
Distribution des abonnements payés vs non payés
Distribution des coûts des abonnements
Identification des abonnements annulés le jour même de la création
3. Visualisations
Histogramme des inscriptions par mois
Boxplot de la durée des abonnements
Diagramme circulaire pour le statut de paiement
4. Analyse des relations
Corrélation entre subscription_cost et duration_days
Boxplot de la durée selon le statut de paiement
Tableau croisé : nombre d’abonnements payés / non payés par mois
5. Analyse probabiliste
Probabilité conditionnelle : P(Annulé | Non payé)
Loi binomiale : probabilité d’un nombre d’annulations donné
Loi normale : probabilité qu’un abonnement dure moins de 30 jours
Théorème de Bayes : probabilité qu’un abonnement soit payé sachant qu’il est annulé
6. Dashboard Streamlit
Affichage interactif des graphiques : histogramme, boxplot, diagramme circulaire
Indicateurs statistiques : durée moyenne, médiane, écart-type, taux de churn
Probabilités clés pour le suivi des abonnements
⚙️ Utilisation
Installer les dépendances :
pip install pandas matplotlib seaborn scipy streamlit
Exécuter le script d’analyse :
python analysis.py
Lancer le dashboard interactif :
streamlit run app.py
📌 Objectifs du code
Comprendre le comportement des abonnés
Identifier les facteurs de churn
Visualiser facilement les tendances et les statistiques
Fournir un outil interactif pour explorer les données