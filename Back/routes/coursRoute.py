from fastapi import APIRouter
from Back.controller import coursController

router = APIRouter()

@router.get("/cours")
def get_list_cours():
    return coursController.getListCours()