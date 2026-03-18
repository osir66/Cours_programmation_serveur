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


@router.get("/")
def get_list_cours():
    return coursController.getListCours()


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

    