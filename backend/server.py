from flask import Flask, jsonify, send_from_directory
from generate_text import generate_planet_description
from config import MAX_PLANETS
import pandas as pd
import os

BACKEND_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_DIR = os.path.join(os.path.dirname(BACKEND_DIR), "frontend")

app = Flask(__name__, static_folder=FRONTEND_DIR, static_url_path="")

df = pd.read_csv(os.path.join(os.path.dirname(BACKEND_DIR), "data/prepared_exoplanets.csv"))

@app.route("/")
def index():
    index_path = os.path.join(FRONTEND_DIR, "index.html")
    if os.path.exists(index_path):
        with open(index_path, "r", encoding="utf-8") as f:
            return f.read()
    return {"error": "index.html not found"}, 404

@app.route("/planets")
def planets():
    planets_data = df[["toi", "pl_rade", "pl_orbper", "pl_trandurh", "pl_trandeplim"]].head(MAX_PLANETS).to_dict(orient="records")
    return jsonify(planets_data)

@app.route("/description/<toi>")
def description(toi):
    desc = generate_planet_description(toi)
    return jsonify({"description": desc})

@app.route("/<path:path>")
def static_proxy(path):
    return send_from_directory(FRONTEND_DIR, path)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
