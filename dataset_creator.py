import pandas as pd
import numpy as np

np.random.seed(42)

data = {
    "Tensions diplomatiques": np.random.choice([1, 0], size=60, p=[0.7, 0.3]),
    "Dépenses militaires en hausse": np.random.choice([1, 0], size=60, p=[0.6, 0.4]),
    "Sanctions économiques": np.random.choice([1, 0], size=60, p=[0.5, 0.5]),
    "Propagande nationale": np.random.choice([1, 0], size=60, p=[0.6, 0.4]),
    "Mouvements de troupes": np.random.choice([1, 0], size=60, p=[0.7, 0.3]),
    "Cyberattaques accrues": np.random.choice([1, 0], size=60, p=[0.5, 0.5]),
    "Crise économique": np.random.choice([1, 0], size=60, p=[0.6, 0.4]),
    "Manifestations massives": np.random.choice([1, 0], size=60, p=[0.5, 0.5]),
    "Ressources stratégiques en jeu": np.random.choice([1, 0], size=60, p=[0.4, 0.6]),
    "Alliances militaires actives": np.random.choice([1, 0], size=60, p=[0.6, 0.4]),
    "Situation": ["Conflit élevé"] * 20 + ["Conflit modéré"] * 20 + ["Paix"] * 20
}

df = pd.DataFrame(data)
df.to_csv("dataset_conflit.csv", index=False)

print("✅ Dataset créé et enregistré sous dataset_conflit.csv")
