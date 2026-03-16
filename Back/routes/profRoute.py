from fastapi import APIRouter
from pydantic import BaseModel
from Back.controller import profController

router = APIRouter() # Tu peux enlever le préfixe pour le moment pour que ça corresponde à tes images

# --- C'est CETTE partie qui dit à Swagger d'afficher les champs de texte ---
class ProfCreate(BaseModel):
    nom: str
    prenom: str
# --------------------------------------------------------------------------

@router.get("/getListProfs", summary="Récupère la liste de tous les professeurs")
def get_list_prof():
    return profController.getListProf()

# --- Et c'est CETTE ligne qui lie le modèle à la route ---
@router.post("/addProf", summary="Ajoute un professeur")
def add_prof(prof: ProfCreate): # Le "prof: ProfCreate" est crucial !
    return profController.CreateProf(prof.nom, prof.prenom)

@router.put("/UpdateProfs/{prof_id}")
def update_prof(prof_id: int, nom: str = None, prenom: str = None):
    return profController.UpdateProf(prof_id, nom, prenom)
