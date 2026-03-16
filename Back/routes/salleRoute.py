from fastapi import APIRouter
from pydantic import BaseModel
from Back.controller import salleController

router = APIRouter(prefix="/salles", tags=["Salles"])

# On met à jour les noms ici aussi !
class SalleCreate(BaseModel):
    nom_salle: str
    capacite: int

@router.get("/")
def get_list_salles():
    return salleController.getListSalles()

@router.post("/")
def add_salle(salle: SalleCreate):
    return salleController.CreateSalle(salle.nom_salle, salle.capacite)