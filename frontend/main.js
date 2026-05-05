document.addEventListener("DOMContentLoaded", async () => {
    const select = document.getElementById("planet-select");
    const descDiv = document.getElementById("planet-description");

    let allPlanets = [];

    // Récupération des planètes
    // 
    const res = await fetch("/planets?limit=25000");
    allPlanets = await res.json();

    function populateSelect(planets) {
        select.innerHTML = '<option value="">Select an exoplanet</option>';
        planets.forEach(p => {
            const opt = document.createElement("option");
            opt.value = p.name;
            opt.textContent = p.name;
            select.appendChild(opt);
        });
    }

    populateSelect(allPlanets);

    window.filterMission = function(mission) {
        document.querySelectorAll('.filter-btn').forEach(btn => btn.classList.remove('active'));
        document.getElementById(`filter-${mission === 'all' ? 'all' : mission.toLowerCase()}`).classList.add('active');

        if (mission === 'all') {
            populateSelect(allPlanets);
        } else {
            populateSelect(allPlanets.filter(p => p.source === mission));
        }
    }

    const loadingMessages = [
        "🔭 Analyzing atmospheric data…",
        "🛰️ Cross-checking with NASA Exoplanet Archive…",
        "💫 Interpreting cosmic signals…",
        "🔭 Initializing AXiA analysis protocol...",
        "Retrieving stellar and orbital data from NASA archives...",
        "Parsing exoplanet parameters: radius, mass, temperature...",
        "Cross-checking with Kepler and TESS mission datasets...",
        "Estimating atmospheric composition...",
        "Detecting potential biosignatures (H₂O, O₂, CH₄)...",
        "Calculating surface gravity and equilibrium temperature...",
        "Evaluating stellar radiation impact...",
        "Running habitability index model...",
        "Compiling findings and generating summary..."
    ];

    select.addEventListener("change", async () => {
        const name = select.value;
        if (!name) {
            descDiv.textContent = "";
            return;
        }

        descDiv.textContent = "";
        descDiv.style.opacity = "0";

        const showMessage = (msg, delay) => {
            return new Promise(resolve => {
                setTimeout(() => {
                    descDiv.style.opacity = "0";
                    setTimeout(() => {
                        descDiv.textContent = msg;
                        descDiv.style.transition = "opacity 0.8s ease";
                        descDiv.style.opacity = "1";
                    }, 300);
                    resolve();
                }, delay);
            });
        };

        for (let i = 0; i < loadingMessages.length; i++) {
            await showMessage(loadingMessages[i], 1500);
        }

        try {
            const res = await fetch(`/description/${encodeURIComponent(name)}`);
            const data = await res.json();

            descDiv.style.opacity = "0";
            setTimeout(() => {
                descDiv.textContent = data.description;
                descDiv.style.transition = "opacity 1s ease";
                descDiv.style.opacity = "1";
            }, 500);

        } catch (e) {
            descDiv.textContent = "⚠️ Error generating description.";
            console.error(e);
        }
    });
});