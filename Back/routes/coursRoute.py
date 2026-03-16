from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime
from Back.controller import coursController

router = APIRouter(prefix="/cours", tags=["Planning"])

class CoursCreate(BaseModel):
    matiere: str
    date_debut: datetime
    date_fin: datetime
    duree_total: datetime # Même si c'est une durée, on respecte ton modèle SQLModel
    id_promo: int
    id_salle: int
    id_prof: int

@router.get("/")
def get_list_cours():
    return coursController.getListCours()

@router.post("/")
def add_cours(cours: CoursCreate):
    # On convertit les datetime en string (texte) car SQLite préfère stocker les dates sous ce format
    return coursController.CreateCours(
        cours.matiere, 
        str(cours.date_debut), 
        str(cours.date_fin), 
        str(cours.duree_total), 
        cours.id_promo, 
        cours.id_salle, 
        cours.id_prof
    )
