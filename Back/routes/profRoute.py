
from fastapi import APIRouter
from Back.controller import profController

router = APIRouter()

@router.get("/profs")
def get_list_prof():
	return profController.getListProf()

