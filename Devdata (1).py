# Importer les bibliothèques nécessaires
import pandas as pd
import matplotlib.pyplot as plt

# Charger le jeu de données
url = "C:/Users/yazid/OneDrive/Bureau/bachelor/Devdata/projet/sujet/Projetanalysede_donnees/data.csv" 
df = pd.read_csv(url)
# Calculer la moyenne d'assistance par sport et quartier
mean_attendance = df.groupby(['Sports Played', 'Borough Location'])['Attendance Sum'].mean().reset_index()

# Préparer la visualisation
plt.figure(figsize=(12, 6))

# Parcourir chaque sport pour créer un graphique en barres par quartier
for sport in mean_attendance['Sports Played'].unique():
    # Sélectionner les données pour le sport actuel
    sport_data = mean_attendance[mean_attendance['Sports Played'] == sport]

    # Créer un graphique en barres pour le sport dans chaque quartier
    plt.bar(sport_data['Borough Location'], sport_data['Attendance Sum'], label=sport, alpha=0.7)

# Ajouter des labels et un titre au graphique
plt.xlabel('Quartier')
plt.ylabel('Moyenne d\'assistance hebdomadaire')
plt.title('Moyenne d\'assistance hebdomadaire par sport dans différents quartiers')

# Ajouter une légende pour identifier chaque sport
plt.legend()

# Afficher le graphique
plt.show()


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

file_path = "C:/Users/yazid/OneDrive/Bureau/bachelor/Devdata/projet/sujet/Projetanalysede_donnees/data.csv"

# Charger le jeu de données depuis un fichier local
df = pd.read_csv(file_path)

# Convertir les colonnes de dates au format datetime
df['Week Start Date'] = pd.to_datetime(df['Week Start Date'])
df['Week End Date'] = pd.to_datetime(df['Week End Date'])

# Calculer la moyenne d'assistance hebdomadaire pour chaque sport dans différents quartiers
sport_avg_attendance = df.groupby(['Sports Played', 'Borough Location'])['Attendance Sum'].mean().reset_index()

# Tracer le graphique à barres
plt.figure(figsize=(14, 8))
sns.barplot(x='Borough Location', y='Attendance Sum', hue='Sports Played', data=sport_avg_attendance)
plt.title('Moyenne d\'assistance hebdomadaire pour chaque sport dans différents quartiers')
plt.xlabel('Quartiers')
plt.ylabel('Moyenne d\'assistance')
plt.legend(title='Sports joués', bbox_to_anchor=(1, 1))

# Afficher le graphique
plt.show()



# Convertir les colonnes de date en objets datetime
df['Week Start Date'] = pd.to_datetime(df['Week Start Date'])
df['Week End Date'] = pd.to_datetime(df['Week End Date'])

# Grouper par semaine et calculer la somme d'assistance
weekly_attendance = df.groupby(['Week Start Date'])['Attendance Sum'].sum().reset_index()

# Visualiser les résultats
plt.figure(figsize=(12, 6))
plt.plot(weekly_attendance['Week Start Date'], weekly_attendance['Attendance Sum'])
plt.xlabel('Semaine')
plt.ylabel('Somme d\'assistance hebdomadaire')
plt.title('Tendances saisonnières dans la participation aux programmes sportifs d\'été')
plt.show()


# In[15]:


# Grouper par parc et calculer la somme d'assistance
park_attendance = df.groupby(['Park Location'])['Attendance Sum'].sum().reset_index()

# Trier les parcs par ordre décroissant d'assistance
park_attendance = park_attendance.sort_values(by='Attendance Sum', ascending=False)

# Visualiser les résultats avec des étiquettes pivotées
plt.figure(figsize=(12, 6))
plt.bar(park_attendance['Park Location'][:10], park_attendance['Attendance Sum'][:10])
plt.xlabel('Parc')
plt.ylabel("Somme d'assistance totale")
plt.title('Top 10 des parcs avec la plus forte participation globale')
plt.xticks(rotation=45, ha='right')  # Rotation des étiquettes
plt.tight_layout()  # Ajustement automatique de la disposition pour éviter les coupures
plt.show()

# Grouper par sport et jour de la semaine, calculer la moyenne d'assistance
sport_day_avg_attendance = df.groupby(['Sports Played', df['Week Start Date'].dt.day_name()])['Attendance Sum'].mean().reset_index()

# Trouver le jour de la semaine avec la plus forte moyenne d'assistance pour chaque sport
popular_days = sport_day_avg_attendance.loc[sport_day_avg_attendance.groupby('Sports Played')['Attendance Sum'].idxmax()]

# Créer un graphique à barres avec des barres plus larges et des étiquettes Y
plt.figure(figsize=(24, 12))
sns.barplot(x='Sports Played', y='Attendance Sum', hue='Week Start Date', data=popular_days, errorbar=None, dodge=True)
# Ajouter des étiquettes à l'axe Y pour améliorer la lisibilité
plt.yticks(fontsize=12)

# Utiliser des barres plus larges pour améliorer la lisibilité
bar_width = 0.7
for bar in plt.gca().patches:
    bar.set_width(bar_width)

plt.title('Journée de la semaine la plus populaire pour chaque sport', fontsize=16)
plt.ylabel('Moyenne d\'assistance', fontsize=14)
plt.xlabel('Sport', fontsize=14)
plt.legend(title='Jour de la semaine', bbox_to_anchor=(1, 1), fontsize=12)
plt.xticks(rotation=90, ha='right', fontsize=12)

# Afficher le résultat
plt.show()