from fastapi import APIRouter
from Back.controller import promotionController

router = APIRouter()

@router.get("/getListPromotions")
def get_list_promotion():
    """Récupère la liste de toutes les promotions existantes."""
    return promotionController.getListPromotion()

@router.post("/addPromotion")
def add_promotion(nom: str, annee: int):
    """
    Crée une nouvelle promotion.
    Exemple : nom="Master 2", annee=2026
    """
    return promotionController.createPromotion(nom, annee)