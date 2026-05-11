import pandas as pd
from datetime import datetime

# Exemple de données (test)
data = {
    "date": [datetime.now()],
    "train": ["TEST123"],
    "retard_min": [5]
}

df = pd.DataFrame(data)

# Sauvegarde Excel
df.to_excel("retards.xlsx", index=False)

print("✅ Fichier Excel généré")
