from fastapi import APIRouter
from pydantic import BaseModel
from Back.controller import salleController

router = APIRouter(prefix="/salles", tags=["Salles"])




class SalleCreate(BaseModel):
    nom_salle: str
    capacite: int

# route pour récupérer la liste de toutes les salles
@router.get("/getListSalles", summary="Récupérer la liste de toutes les salles (back-end) ")
def get_list_salles():
    return salleController.getListSalles()

# Route pour ajouter une salle
@router.post("/createSalle", summary="Ajouter une salle (back-end) ")
def add_salle(salle: SalleCreate):
    return salleController.CreateSalle(salle.nom_salle, salle.capacite)

# Route pour modifier une salle
@router.put("/updateSalle/{id_salle}", summary="Modifier une salle (back-end)")
def update_salle(id_salle: int, salle: SalleCreate):
    return salleController.updateSalle(id_salle, salle.nom_salle, salle.capacite)

# Route pour supprimer une salle
@router.delete("/deleteSalle/{id_salle}", summary="Supprimer une salle (back-end)")
def delete_salle(id_salle: int):
    return salleController.deleteSalle(id_salle)
