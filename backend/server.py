from flask import Flask, jsonify, send_from_directory
from generate_text import generate_planet_description, get_planets_list

app = Flask(__name__, static_folder="frontend")

@app.route("/")
def index():
    return send_from_directory("frontend", "index.html")

@app.route("/planets")
def planets():
    return jsonify(get_planets_list())

@app.route("/description/<toi>")
def description(toi):
    desc = generate_planet_description(toi)
    return jsonify({"description": desc})

@app.route("/<path:path>")
def static_proxy(path):
    return send_from_directory("frontend", path)

if __name__ == "__main__":
    app.run(debug=True, port=8000)