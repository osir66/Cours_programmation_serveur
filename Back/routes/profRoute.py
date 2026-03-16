
from fastapi import APIRouter, Request, HTTPException
from Back.controller import profController

router = APIRouter()

@router.get("/getListProfs", summary="Récupère la liste de tous les professeurs")
def get_list_prof():
	return profController.getListProf()

@router.post("/addProf")
async def add_prof(request: Request):
    try:
        data = await request.json()
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid JSON")
    nom = data.get('nom')
    prenom = data.get('prenom')
    if not nom or not prenom:
        raise HTTPException(status_code=400, detail="'nom' and 'prenom' are required")
    return profController.CreateProf(nom, prenom)

@router.put("/UpdateProfs/{prof_id}", summary="Met à jour les informations d'un professeur")
def update_prof(prof_id: int, nom: str = None, prenom: str = None):
    return profController.UpdateProf(prof_id, nom, prenom)
