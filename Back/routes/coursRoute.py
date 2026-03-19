
from fastapi import APIRouter
from pydantic import BaseModel
from Back.controller import coursController


router = APIRouter(prefix="/cours", tags=["Planning"])


class CoursCreate(BaseModel):
    matiere: str
    date_debut: str
    date_fin: str
    duree_total: str
    id_promo: int
    id_salle: int
    id_prof: int


# Route pour récupérer la liste de tous les cours
@router.get("/getListCours", summary="Récupérer la liste de tous les cours")
def get_list_cours():
    return coursController.getListCours()


# Route pour ajouter un cours
@router.post("/addCours")
def add_cours(cours: CoursCreate):
    return coursController.CreateCours(
        cours.matiere,
        cours.date_debut,
        cours.date_fin,
        cours.duree_total,
        cours.id_promo,
        cours.id_salle,
        cours.id_prof
    )


# Route pour modifier un cours
@router.put("/updateCours/{id_cours}", summary="Modifier un cours")
def update_cours(id_cours: int, cours: CoursCreate):
    return coursController.updateCours(
        id_cours,
        cours.matiere,
        cours.date_debut,
        cours.date_fin,
        cours.duree_total,
        cours.id_promo,
        cours.id_salle,
        cours.id_prof
    )


# Route pour supprimer un cours
@router.delete("/deleteCours/{id_cours}", summary="Supprimer un cours")
def delete_cours(id_cours: int):
    return coursController.deleteCours(id_cours)

    