
from fastapi import APIRouter
from pydantic import BaseModel
from Back.controller import profController

router = APIRouter()



class ProfCreate(BaseModel):
    nom: str
    prenom: str



#route pour récupérer la liste de tous les professeurs
@router.get("/getListProfs", summary="Récupère la liste de tous les professeurs")
def get_list_prof():
    return profController.getListProf()


#route pour ajouter un professeur
@router.post("/addProf", summary="Ajoute un professeur")
def add_prof(prof: ProfCreate):
    return profController.CreateProf(prof.nom, prof.prenom)


#route pour modifier un professeur 
@router.put("/UpdateProfs/{prof_id}")
def update_prof(
    prof_id: int,
    nom: str = None,
    prenom: str = None
):
    return profController.UpdateProf(prof_id, nom, prenom)

#route pour supprimer un professeur
@router.delete("/deleteProf/{prof_id}")
def delete_prof(prof_id: int):
    return profController.deleteProf(prof_id)
