from fastapi import APIRouter
from Back.controller import coursController

router = APIRouter()

@router.get("/cours", summary="Récupère la liste de tous les cours")
def get_list_cours():
    return coursController.getListCours()

@router.post("/addCours", summary="Crée un nouveau cours")
def add_cours(matière: str, prof_id: int, durée: int, id_salle: int, date_heure: str, id_promo: int):
    return coursController.CreateCours(matière, prof_id, durée, id_salle, date_heure, id_promo)

@router.put("/UpdateCours/{cours_id}", summary="Met à jour les informations d'un cours")
def update_cours(cours_id: int, matière: str = None, prof_id: int = None, durée: int = None, id_salle: int = None, date_heure: str = None, id_promo: int = None):
    return coursController.UpdateCours(cours_id, matière, prof_id, durée, id_salle, date_heure, id_promo)

@router.delete("/deleteCours/{cours_id}", summary="Supprime un cours de la liste")
def delete_cours(cours_id: int):
    return coursController.deleteCours(cours_id)
