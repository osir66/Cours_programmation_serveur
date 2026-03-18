from fastapi import APIRouter
from pydantic import BaseModel
from Back.controller import promotionController

router = APIRouter(prefix="/promotions", tags=["Promotions"])

# On met à jour avec nom_promotion et annee (qui est un int)


class PromotionCreate(BaseModel):
    nom_promotion: str
    annee: int

#route pour récupérer la liste de toutes les promotions
@router.get("/getListPromotions")
def get_list_promotions():
    return promotionController.getListPromotions()

#route pour ajouter une promotion
@router.post("/createPromotion")
def add_promotion(promo: PromotionCreate):
    return promotionController.CreatePromotion(
        promo.nom_promotion, promo.annee
    )

#route pour modifier une promotion
@router.put("/updatePromotion/{id_promo}")
def update_promotion(id_promo: int, promo: PromotionCreate):
    return promotionController.updatePromotion(
        id_promo, promo.nom_promotion, promo.annee
    )

#route pour supprimer une promotion
@router.delete("/deletePromotion/{id_promo}")
def delete_promotion(id_promo: int):
    return promotionController.deletePromotion(id_promo)    
