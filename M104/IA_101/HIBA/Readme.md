# 🎓 Analyse de la Performance des Étudiants (Student Performance)

Ce projet propose une analyse statistique approfondie des scores d'étudiants (Mathématiques, Lecture, Écriture) à partir d'un fichier CSV. L'objectif est d'explorer les tendances centrales, la dispersion des données et d'identifier les facteurs socio-économiques qui influencent la réussite scolaire.

## 🛠️ Technologies Utilisées

* **Python 3.x**
* **Pandas** : Manipulation des DataFrames et nettoyage des données.
* **NumPy** : Calculs mathématiques et vectoriels.
* **Plotly** : Créations de visualisations interactives.

---

## 📂 Structure des Exercices

### EXERCICE 1 : Mesures de Tendance Centrale
* Calcul de la **Moyenne**, **Médiane**, et du **Mode**.
* **Analyse de distribution** : Comparaison des mesures pour déduire l'asymétrie (Skewness).
    * Si $Moyenne > Médiane$ : Asymétrie positive (Skewed right).
    * Si $Moyenne < Médiane$ : Asymétrie négative (Skewed left).



### EXERCICE 2 : Dispersion des Données
* **Étendue (Range)** : Écart total entre le score maximum et minimum.
* **Variance ($\sigma^2$)** et **Écart-type ($\sigma$)** : Mesure de la dispersion des notes autour de la moyenne.

### EXERCICE 3 : Quartiles et Valeurs Aberrantes
* Calcul de l'**IQR** (Interquartile Range) : $Q3 - Q1$.
* **Détection des Outliers** : Identification des scores atypiques via la méthode de Tukey :
  $$[Q1 - 1.5 \times IQR, \ Q3 + 1.5 \times IQR]$$

### EXERCICE 4 : Visualisation Interactive (Plotly)
Pour une compréhension visuelle complète, trois types de graphiques sont générés :
* **Histogrammes** : Pour observer la forme de la distribution globale.
* **Box Plots (Boîtes à moustaches)** : Pour visualiser les quartiles et confirmer la présence des valeurs aberrantes (outliers) détectées à l'exercice 3.
* **Graphiques en Barres** : Pour comparer les performances moyennes entre différents groupes.



[Image of boxplot showing outliers and interquartile range]


### EXERCICE 5 : Analyse Croisée et Insights 🔍
#### a) Corrélation entre les matières
Calcul du **Coefficient de Pearson ($r$)** pour évaluer la force du lien entre les scores :
$$r = \frac{\sum(x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum(x_i - \bar{x})^2 \cdot \sum(y_i - \bar{y})^2}}$$

| Valeur de $r$ | Force | Signification |
| :--- | :--- | :--- |
| 0.7 - 1.0 | Forte | Relation très marquée |
| 0.4 - 0.7 | Modérée | Relation significative |
| 0.0 - 0.4 | Faible | Relation peu marquée |

#### b) Facteurs Influentiels
Analyse de l'impact des variables catégorielles :
* **Parental level of education** : Impact du milieu familial.
* **Lunch** : Influence du statut socio-économique.
* **Test preparation course** : Analyse de l'efficacité du soutien scolaire.
* **Gender & Race/Ethnicity** : Étude de la diversité des résultats.

---

## 🚀 Installation et Utilisation

1. **Cloner le projet** :
   ```bash
   git clone [https://github.com/votre-nom-utilisateur/student-performance-analysis.git](https://github.com/votre-nom-utilisateur/student-performance-analysis.git))
