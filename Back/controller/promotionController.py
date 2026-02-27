# Back/controller/promotionController.py

# La table est ici !
tablePromotion = [
    {"id": 1, "nom": "Bachelor 1", "annee": 2026},
    {"id": 2, "nom": "Bachelor 2", "annee": 2026},
    {"id": 3, "nom": "Master 1", "annee": 2026}
]

def getListPromotion():
    return tablePromotion

def createPromotion(nom, annee):
    new_id = max((p["id"] for p in tablePromotion), default=0) + 1
    new_promo = {"id": new_id, "nom": nom, "annee": annee}
    tablePromotion.append(new_promo)
    return new_promo