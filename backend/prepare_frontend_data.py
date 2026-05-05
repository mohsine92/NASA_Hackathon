import pandas as pd
import json
import subprocess

if __name__ == "__main__":
    # Lire le CSV préparé
    df = pd.read_csv("data/prepared_exoplanets.csv")
    planets = []

    for idx, row in df.iterrows():
        name = row['toi']
        radius = row['pl_rade'] / 5  # mise à l'échelle pour affichage

        # Générer la description via Mistral / Ollama
        prompt = f"Explique en termes simples l'exoplanète {name}. Elle a un rayon de {row['pl_rade']} fois celui de la Terre, une période orbitale de {row['pl_orbper']} jours, et une durée de transit de {row['pl_trandurh']} heures. Fais une description vulgarisée pour le grand public."

        try:
            result = subprocess.run(
                ["ollama", "run", "mistral"],
                input=prompt,
                capture_output=True,
                text=True,
                check=True
            )
            description = result.stdout.strip()
        except Exception as e:
            description = f"Erreur lors de l'appel à Mistral: {e}"

        planets.append({
            "name": str(name),
            "radius": radius,
            "description": description
        })

    # Sauvegarde JSON pour le front-end
    with open("data/planets.json", "w", encoding="utf-8") as f:
        json.dump(planets, f, ensure_ascii=False, indent=2)

    print(f"✅ {len(planets)} planètes générées et sauvegardées.")