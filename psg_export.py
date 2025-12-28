import pandas as pd

url = "https://fbref.com/en/squads/e2d8892c/2024-2025/all_comps/Paris-Saint-Germain-Stats-All-Competitions"
tables = pd.read_html(url)

# Afficher tous les noms de colonnes pour voir ce qu'on récupère
for i, table in enumerate(tables):
    print(f"Tableau {i} (colonnes) : {table.columns.tolist()}")

df = tables[0]  # Change l’index si nécessaire

# ✅ Corriger MultiIndex avant export Excel
df.columns = [' '.join(col).strip() if isinstance(col, tuple) else col for col in df.columns]

# Sauvegarde Excel
df.to_excel("psg_stats_2024_2025.xlsx", index=False)

print("✅ Export terminé, fichier prêt !")
