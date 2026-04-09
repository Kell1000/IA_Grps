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

### EXERCICE 5 : Analyse Croisée et Insights
* **Corrélation de Pearson ($r$)** : Mesure de la force de la relation entre les matières (ex: Math vs Lecture).
  * $0.7 - 1.0$ : Forte | $0.4 - 0.7$ : Modérée | $0.0 - 0.4$ : Faible.
* **Analyse des Facteurs Influents** : Étude de l'impact des variables socio-économiques sur les scores :
    * `Parental level of education` : Impact du milieu académique familial.
    * `Lunch` : Influence du statut économique (standard vs réduit).
    * `Test preparation course` : Efficacité réelle du suivi de cours de préparation.

---

## 🚀 Installation et Utilisation

1. **Cloner le projet** :
   ```bash
   git clone [https://github.com/votre-nom-utilisateur/student-performance-analysis.git](https://github.com/votre-nom-utilisateur/student-performance-analysis.git))
