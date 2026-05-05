# AXiA – Exoplanet Explorer | NASA International Space Apps Challenge 2025

<div align="center">
  <img width="700" height="auto" alt="banner_nasa_hackh" src="https://github.com/user-attachments/assets/733166eb-c4f5-4905-943f-a81f08eb9707" />
  <img width="700" height="auto" src="https://github.com/user-attachments/assets/5b2d2dd0-4129-4dff-a3cc-3bcdc3a01703" />
</div>   

---

**AXiA** is an interactive web platform that transforms **17,000+ NASA exoplanet entries from TESS and Kepler missions** into real-time, AI-generated educational descriptions — making complex astronomical data accessible to the general public.

---

## Problem Solved

Raw NASA exoplanet datasets are dense and technical, making them difficult for non-specialists to understand. AXiA solves this by using a **data-to-text LLM pipeline** that automatically converts physical measurements (radius, orbital period, transit duration) into clear, scientifically accurate, and engaging narratives.

---

## How It Works

1. User selects an exoplanet from a dynamic dropdown menu
2. The backend retrieves its physical data from NASA TESS/Kepler datasets
3. A prompt is constructed and sent to **MGroq**
4. A real-time educational description is generated and displayed

---

## 🛠 Technologies

- **Frontend:** JavaScript, HTML, CSS
- **Backend:** Python + Flask
- **AI:** Groq
- **Data sources:** NASA TESS (~1,000+ entries) + Kepler (~16,000+ entries)

---

## ⚡ Installation & Run

### Prerequisites

- Python 3.12+

### Steps

```bash
git clone https://github.com/mohsine92/NASA_Hackathon.git
cd NASA_Hackathon
pip install -r requirements.txt
python3 backend/server.py
```

Then open your browser at `http://localhost:5000`

---

## Project Structure

```
NASA_Hackathon/
├── backend/
│   ├── server.py
│   ├── generate_text.py
│   ├── mistral_client.py
│   ├── prepare_frontend_data.py
│   └── config.py
├── frontend/
│   ├── index.html
│   ├── main.js
│   ├── style.css
│   └── planets.json
├── data/
├── .env.example
├── Makefile
├── requirements.txt
└── README.md
```

---

## Educational Impact

- Makes complex astronomical data accessible to students and the public
- Serves as a teaching tool for STEM education
- Demonstrates how LLMs can bridge raw scientific data and public understanding
- Built in 48 hours for the NASA International Space Apps Challenge 2025

---

## AI Compliance

AXiA uses Groq exclusively for generating educational descriptions based on NASA data. All AI-generated text is clearly labeled in the UI. AI is not used to modify NASA branding or copyrighted material.

---

## Author

**Mohsine Essat** — [GitHub](https://github.com/mohsine92) · [LinkedIn](https://www.linkedin.com/in/mohsine-essat/)
