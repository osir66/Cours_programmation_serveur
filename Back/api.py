from fastapi import FastAPI
from fastapi.responses import FileResponse
from pathlib import Path
from Back.routes import profRoute, coursRoute, salleRoute, promotionRoute

app = FastAPI()

# Enregistrer tous les routers disponibles pour qu'ils apparaissent dans la doc (/docs)
app.include_router(profRoute.router)
app.include_router(coursRoute.router)
app.include_router(salleRoute.router)
app.include_router(promotionRoute.router)

# --- GESTION DES CHEMINS FRONT-END ---
BASE_DIR = Path(__file__).resolve().parent.parent
# On pointe directement vers le dossier Front
FRONT_DIR = BASE_DIR / "Front"

# On déclare les futurs fichiers HTML
code_creation_prof = FRONT_DIR / "create_prof.html"
code_planning = FRONT_DIR / "planning.html"
code_creation_cours = FRONT_DIR / "create_cours.html"

# --- ROUTES POUR AFFICHER LES PAGES WEB ---

@app.get("/prof")
def get_prof_page():
    if code_creation_prof.exists():
        return FileResponse(str(code_creation_prof))
    return {"message": "Le fichier HTML des profs est introuvable."}

@app.get("/")
def get_planning_page():
    if code_planning.exists():
        return FileResponse(str(code_planning))
    return {
        "message": (
            "La route est prête, mais le fichier planning.html n'existe pas encore !"
        )
    }

@app.get("/cour")
def get_cours_page():
    if code_creation_cours.exists():
        return FileResponse(str(code_creation_cours))
    return {"message": "Le fichier HTML des cours est introuvable."}