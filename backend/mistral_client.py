import subprocess

def get_mistral_response(prompt: str) -> str:
    """
    Envoie une requête au modèle Mistral via Ollama et récupère la réponse.
    """
    try:
        # ollama run lit le prompt depuis stdin
        result = subprocess.run(
            ["ollama", "run", "mistral"],
            input=prompt,
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            print("Erreur Ollama :", result.stderr)
            return "Impossible de récupérer la description."
        return result.stdout.strip()
    except Exception as e:
        print("Erreur lors de l'appel à Ollama :", e)
        return "Impossible de récupérer la description."