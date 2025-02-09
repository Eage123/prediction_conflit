import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Charger le dataset
df = pd.read_csv("dataset_conflit.csv")

# Séparer les features et la cible
X = df.drop("Situation", axis=1)
y = df["Situation"]

# Division en train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Entraîner le modèle
model = RandomForestClassifier(n_estimators=200, max_depth=10, min_samples_split=2, random_state=42)
model.fit(X_train, y_train)

# Sauvegarder le modèle
joblib.dump(model, "model_conflit.pkl")

print("✅ Modèle entraîné et enregistré sous model_conflit.pkl")