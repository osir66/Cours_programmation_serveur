# Simulation de la tableSalle (à remplacer par une DB plus tard)
tableSalle = [
    {"id": 1, "nom": "A101", "capacite": 30},
    {"id": 2, "nom": "B204", "capacite": 20},
    {"id": 3, "nom": "Amphi Delta", "capacite": 150}
]

def getListSalle():
    """Retourne la liste de toutes les salles."""
    return tableSalle

def getOneSalle(salle_id):
    """Retourne une salle spécifique par son ID."""
    for salle in tableSalle:
        if salle["id"] == salle_id:
            return salle
    return None

def createSalle(nom, capacite):
    """Crée une nouvelle salle."""
    # Gestion de l'ID si la table est vide
    new_id = max((salle["id"] for salle in tableSalle), default=0) + 1
    new_salle = {"id": new_id, "nom": nom, "capacite": capacite}
    tableSalle.append(new_salle)
    return new_salle

def updateSalle(salle_id, nom=None, capacite=None):
    """Met à jour une salle existante."""
    for salle in tableSalle:
        if salle["id"] == salle_id:
            if nom is not None:
                salle["nom"] = nom
            if capacite is not None:
                salle["capacite"] = capacite
            return salle
    return None

def deleteSalle(salle_id):
    """Supprime une salle."""
    global tableSalle
    tableSalle = [salle for salle in tableSalle if salle["id"] != salle_id]
    return {"message": f"Salle {salle_id} supprimée."}