from fastapi import APIRouter
from pydantic import BaseModel
from Back.controller import promotionController

router = APIRouter(prefix="/promotions", tags=["Promotions"])

# On met à jour avec nom_promotion et annee (qui est un int)


class PromotionCreate(BaseModel):
    nom_promotion: str
    annee: int

# Route pour récupérer la liste de toutes les promotions
@router.get("/getListPromotions", summary="Récupérer la liste de toutes les promotions (back-end)")
def get_list_promotions():
    return promotionController.getListPromotions()

# Route pour ajouter une promotion
@router.post("/createPromotion", summary="Ajouter une promotion (back-end)")
def add_promotion(promo: PromotionCreate):
    return promotionController.CreatePromotion(
        promo.nom_promotion, promo.annee
    )

# Route pour modifier une promotion
@router.put("/updatePromotion/{id_promo}", summary="Modifier une promotion (back-end)")
def update_promotion(id_promo: int, promo: PromotionCreate):
    return promotionController.updatePromotion(
        id_promo, promo.nom_promotion, promo.annee
    )

# Route pour supprimer une promotion
@router.delete("/deletePromotion/{id_promo}", summary="Supprimer une promotion (back-end)")
def delete_promotion(id_promo: int):
    return promotionController.deletePromotion(id_promo)    
