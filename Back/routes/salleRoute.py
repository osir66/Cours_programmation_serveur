from fastapi import APIRouter, HTTPException
from Back.controller import salleController

router = APIRouter()

@router.get("/getListSalles",summary="Récupère la liste de toutes les salles")
def get_list_salle():
    """Récupère la liste de toutes les salles."""
    return salleController.getListSalle()

@router.get("/getOneSalle/{salle_id}",summary="Récupère une salle spécifique par son ID")
def get_one_salle(salle_id: int):
    """Récupère une salle spécifique par son ID."""
    salle = salleController.getOneSalle(salle_id)
    if not salle:
        raise HTTPException(status_code=404, detail="Salle non trouvée")
    return salle

@router.post("/addSalle", summary="Ajoute une nouvelle salle")
def add_salle(nom: str, capacite: int):
    """Ajoute une nouvelle salle."""
    return salleController.createSalle(nom, capacite)

@router.put("/updateSalle/{salle_id}",summary="Met à jour les informations d'une salle")
def update_salle(salle_id: int, nom: str = None, capacite: int = None):
    """Met à jour les informations d'une salle."""
    salle = salleController.updateSalle(salle_id, nom, capacite)
    if not salle:
        raise HTTPException(status_code=404, detail="Salle non trouvée")
    return salle

@router.delete("/deleteSalle/{salle_id}",summary="Supprime une salle de la liste")
def delete_salle(salle_id: int):
    """Supprime une salle de la liste."""
    # On peut vérifier si elle existe avant de supprimer pour être propre
    return salleController.deleteSalle(salle_id)