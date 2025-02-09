import streamlit as st
import numpy as np
import joblib

# Charger le modèle
model = joblib.load("model_conflit.pkl")

# Titre de l'application
st.title("Prédiction de Conflit")
st.write("Sélectionnez les facteurs de risque et obtenez une prévision.")

# Interface utilisateur
features = {
    "Tensions diplomatiques": st.checkbox("Tensions diplomatiques"),
    "Dépenses militaires en hausse": st.checkbox("Dépenses militaires en hausse"),
    "Sanctions économiques": st.checkbox("Sanctions économiques"),
    "Propagande nationale": st.checkbox("Propagande nationale"),
    "Mouvements de troupes": st.checkbox("Mouvements de troupes"),
    "Cyberattaques accrues": st.checkbox("Cyberattaques accrues"),
    "Crise économique": st.checkbox("Crise économique"),
    "Manifestations massives": st.checkbox("Manifestations massives"),
    "Ressources stratégiques en jeu": st.checkbox("Ressources stratégiques en jeu"),
    "Alliances militaires actives": st.checkbox("Alliances militaires actives")
}

# Préparation des données pour le modèle
input_data = [int(value) for value in features.values()]
input_data = np.array(input_data).reshape(1, -1)

# Prédiction
if st.button("Prédire le conflit"):
    prediction = model.predict(input_data)
    st.write(f"### Niveau de conflit probable : *{prediction[0]}*")
