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
            f"Provide a complete and accessible description of exoplanet {planet['name']} "
            f"from the {planet['source']} mission. "
            f"Radius: {planet['radius']} Earth radii, "
            f"orbital period: {planet['period']} days, "
            f"transit duration: {planet['duration']} hours. "
            "Explain its physical characteristics, orbital conditions, and implications "
            "for composition, potential climate, and habitability. "
            "Make it educational and engaging for students and astronomy enthusiasts. "
            "Reply in English."
        )
        description = get_mistral_response(prompt)
        if not description:
            return "Unable to retrieve description."
        return description
    except Exception as e:
        print("Error generating description for", name, e)
        return "Unable to retrieve description."