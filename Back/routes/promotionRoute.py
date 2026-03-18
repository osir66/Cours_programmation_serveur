from fastapi import APIRouter
from pydantic import BaseModel
from Back.controller import promotionController

router = APIRouter(prefix="/promotions", tags=["Promotions"])

# On met à jour avec nom_promotion et annee (qui est un int)


class PromotionCreate(BaseModel):
    nom_promotion: str
    annee: int


@router.get("/")
def get_list_promotions():
    return promotionController.getListPromotions()


@router.post("/")
def add_promotion(promo: PromotionCreate):
    return promotionController.CreatePromotion(
        promo.nom_promotion, promo.annee
    )
