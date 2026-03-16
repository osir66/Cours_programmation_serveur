from fastapi import FastAPI
from fastapi.responses import FileResponse
from pathlib import Path
from Back.routes import profRoute, coursRoute, salleRoute, promotionRoute

app = FastAPI()

# Enregistrer tous les routers disponibles pour qu'ils apparaissent dans la doc OpenAPI (/docs)
app.include_router(profRoute.router)
app.include_router(coursRoute.router)
app.include_router(salleRoute.router)
app.include_router(promotionRoute.router)

# --- GESTION DES CHEMINS FRONT-END ---
BASE_DIR = Path(__file__).resolve().parent.parent
FRONT_DIR = BASE_DIR / "Front" # On pointe directement vers le dossier Front

# On déclare les futurs fichiers HTML
code_creation_prof = FRONT_DIR / "create_prof.html"
code_planning = FRONT_DIR / "planning.html" # <-- Ta future page pour le planning

# --- ROUTES POUR AFFICHER LES PAGES WEB ---

@app.get("/")
def read_root():
    return {"message": "Hello FastAPI - Bienvenue sur l'API !"}

@app.get("/prof")
def get_prof_page(): # J'ai changé le nom de la fonction ici
    if code_creation_prof.exists():
        return FileResponse(str(code_creation_prof))
    return {"message": "Le fichier HTML des profs est introuvable."}

# La nouvelle route pour ton planning !
@app.get("/planning")
def get_planning_page():
    if code_planning.exists():
        return FileResponse(str(code_planning))
    # Comme tu ne l'as pas encore créé, ça affichera ce message en attendant :
    return {"message": "La route est prête, mais le fichier planning.html n'existe pas encore !"}