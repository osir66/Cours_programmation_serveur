
from fastapi import APIRouter
from Back.controller import profController

router = APIRouter()

@router.get("/getListProfs")
def get_list_prof():
	return profController.getListProf()

@router.post("/addProf")
def add_prof(nom: str, prenom: str):
    return profController.CreateProf(nom, prenom)

@router.put("/UpdateProfs/{prof_id}")
def update_prof(prof_id: int, nom: str = None, prenom: str = None):
    return profController.UpdateProf(prof_id, nom, prenom)
