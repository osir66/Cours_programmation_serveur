
from fastapi import APIRouter
from Back.controller import profController

router = APIRouter()

@router.get("/getListProfs", summary="Récupère la liste de tous les professeurs")
def get_list_prof():
	return profController.getListProf()

@router.post("/addProf", summary="Crée un nouveau professeur")
def add_prof(nom: str, prenom: str):
    return profController.CreateProf(nom, prenom)

@router.put("/UpdateProfs/{prof_id}", summary="Met à jour les informations d'un professeur")
def update_prof(prof_id: int, nom: str = None, prenom: str = None):
    return profController.UpdateProf(prof_id, nom, prenom)
