from fastapi import FastAPI
from fastapi.responses import FileResponse
from pathlib import Path
from Back.routes import profRoute, coursRoute, salleRoute, promotionRoute, userRoute

app = FastAPI()

# Enregistrer tous les routers disponibles pour qu'ils apparaissent dans la doc (/docs)
app.include_router(profRoute.router)
app.include_router(coursRoute.router)
app.include_router(salleRoute.router)
app.include_router(promotionRoute.router)
app.include_router(userRoute.router)

# --- GESTION DES CHEMINS FRONT-END ---
BASE_DIR = Path(__file__).resolve().parent.parent
# On pointe directement vers le dossier Front
FRONT_DIR = BASE_DIR / "Front"

# On déclare les futurs fichiers HTML
code_creation_prof = FRONT_DIR / "create_prof.html"
code_planning = FRONT_DIR / "planning.html"
code_creation_cours = FRONT_DIR / "create_cours_modern.html"
code_index = FRONT_DIR / "index.html"
code_planning_modern = FRONT_DIR / "planning_modern.html"
code_create_salle_modern = FRONT_DIR / "create_salle_modern.html"
code_create_promotion_modern = FRONT_DIR / "create_promotion_modern.html"
code_connexion = FRONT_DIR / "connexion.html"

# --- ROUTES POUR AFFICHER LES PAGES WEB ---

@app.get("/prof", summary="Affiche la page de gestion des professeurs (front) ")
def get_prof_page():
    if code_creation_prof.exists():
        return FileResponse(str(code_creation_prof))
    return {"message": "Le fichier HTML des profs est introuvable."}


# --- PAGE D'ACCUEIL (MENU MODERNE) ---
@app.get("/", summary="Affiche la page d'accueil (front)")
def get_index_page():
    if code_index.exists():
        return FileResponse(str(code_index))
    return {"message": "Le fichier index.html n'existe pas dans Front."}

# --- AUTRES PAGES MODERNES ---
@app.get("/planning",summary="Affiche la page de planning (front)")
def get_planning_page():
    if code_planning.exists():
        return FileResponse(str(code_planning))
    return {"message": "Le fichier planning.html n'existe pas."}

@app.get("/planning_modern",summary="Affiche la page de planning moderne (front)")
def get_planning_modern_page():
    if code_planning_modern.exists():
        return FileResponse(str(code_planning_modern))
    return {"message": "Le fichier planning_modern.html n'existe pas."}

@app.get("/cours", summary="Affiche la page de création des cours (front)")
def get_cours_page():
    if code_creation_cours.exists():
        return FileResponse(str(code_creation_cours))
    return {"message": "Le fichier HTML des cours est introuvable."}

@app.get("/salle", summary="Affiche la page de création des salles (front)")
def get_salle_page():
    if code_create_salle_modern.exists():
        return FileResponse(str(code_create_salle_modern))
    return {"message": "Le fichier HTML des salles est introuvable."}

@app.get("/promotion", summary="Affiche la page de création des promotions (front)")
def get_promotion_page():
    if code_create_promotion_modern.exists():
        return FileResponse(str(code_create_promotion_modern))
    return {"message": "Le fichier HTML des promotions est introuvable."}

@app.get("/cour", summary="Affiche la page de création des cour (front)")
def get_cours_page():
    if code_creation_cours.exists():
        return FileResponse(str(code_creation_cours))
    return {"message": "Le fichier HTML des cours est introuvable."}


@app.get("/connexion", summary="Affiche la page de connexion (front)")
def get_connexion_page():
    if code_connexion.exists():
        return FileResponse(str(code_connexion))
    return {"message": "Le fichier connexion.html est introuvable."}