import pandas as pd
from mistral_client import get_mistral_response
from config import MAX_PLANETS, BASE_DIR
import os

def get_planets_list():
    try:
        csv_path = os.path.join(BASE_DIR, "data", "prepared_exoplanets.csv")
        df = pd.read_csv(csv_path)
        return df[['toi', 'pl_rade', 'pl_orbper', 'pl_trandurh', 'pl_trandeplim']].head(MAX_PLANETS).to_dict(orient='records')
    except Exception as e:
        print("Erreur lors du chargement des planètes :", e)
        return []

def generate_planet_description(toi):
    try:
        planets = get_planets_list()
        planet = next((p for p in planets if str(p["toi"]) == str(toi)), None)
        if not planet:
            return "Planète non trouvée."
        prompt = (
            f"Provide a complete and accessible description of exoplanet {planet['toi']} "
            f"based on NASA TESS and Kepler data. "
            f"Radius: {planet['pl_rade']} Earth radii, "
            f"orbital period: {planet['pl_orbper']} days, "
            f"transit duration: {planet['pl_trandurh']} hours. "
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
        print("Error generating description for", toi, e)
        return "Unable to retrieve description."