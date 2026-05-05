import pandas as pd
from mistral_client import get_mistral_response
from config import MAX_PLANETS, DATA_PATH, BASE_DIR
import os

def get_planets_list():
    try:
        csv_path = os.path.join(BASE_DIR, "data", "combined_exoplanets.csv")
        df = pd.read_csv(csv_path)
        return df[['name', 'radius', 'period', 'duration', 'source']].head(MAX_PLANETS).to_dict(orient='records')
    except Exception as e:
        print("Erreur lors du chargement des planètes :", e)
        return []

def generate_planet_description(name):
    try:
        csv_path = os.path.join(BASE_DIR, "data", "combined_exoplanets.csv")
        df = pd.read_csv(csv_path)
        row = df[df['name'] == name]
        if row.empty:
            return "Planète non trouvée."
        planet = row.iloc[0]
        prompt = (
            f"You are an astronomy educator. Based ONLY on the following confirmed data from the {planet['source']} mission, "
            f"describe exoplanet {planet['name']} in an educational and engaging way for the general public. "
            f"DO NOT add any information not provided below. DO NOT invent mass, constellation, star type, or distance. "
            f"Only use these facts:\n"
            f"- Radius: {planet['radius']} Earth radii\n"
            f"- Orbital period: {planet['period']} days\n"
            f"- Transit duration: {planet['duration']} hours\n"
            f"- Mission: {planet['source']}\n\n"
            f"Explain what these measurements tell us about the planet's size, year length, and what we can infer "
            f"about its potential composition and conditions. Be clear about what is known vs what is inferred. "
            f"Reply in french."
        )
        description = get_mistral_response(prompt)
        if not description:
            return "Unable to retrieve description."
        return description
    except Exception as e:
        print("Error generating description for", name, e)
        return "Unable to retrieve description."