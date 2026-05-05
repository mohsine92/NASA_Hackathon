import json
from mistral_client import get_mistral_response
from config import MAX_PLANETS, DATA_PATH

def get_planets_list():
    try:
        with open(DATA_PATH) as f:
            planets = json.load(f)
        planets_sorted = sorted(planets, key=lambda p: float(p["toi"]))
        return planets_sorted[:MAX_PLANETS]
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
            f"Utilise les données scientifiques de NASA TESS et Kepler pour fournir une analyse complète et compréhensible pour le grand public de l'exoplanète {planet['toi']}. "
            f"L'exoplanète a un rayon de {planet['pl_rade']} fois celui de la Terre, "
            f"une période orbitale de {planet['pl_orbper']} jours, "
            f"et une durée de transit de {planet['pl_trandurh']} heures. "
            "Fournis une description claire de ses caractéristiques physiques, de ses conditions orbitales, et explique les implications possibles pour sa composition, son climat potentiel, et sa habitabilité. "
            "Génère le texte de façon éducative et accessible, en maintenant un niveau scientifique rigoureux, "
            "et rends la lecture engageante pour les étudiants, enseignants, et passionnés d'astronomie. "
            "Mentionne que la description a été générée avec Mistral AI pour une expérience interactive. "
            "Répond en anglais."
        )
        description = get_mistral_response(prompt)
        if not description:
            return "Impossible de récupérer la description."
        return description
    except Exception as e:
        print("Erreur lors de la génération pour", toi, e)
        return "Impossible de récupérer la description."