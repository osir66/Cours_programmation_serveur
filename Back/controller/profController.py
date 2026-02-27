#Toutes les fonctions de gestion des professeurs dans ce fichier

# Simuler une tableProf (à remplacer par une vraie base de données plus tard)
tableProf = [
	{"id": 1, "nom": "Dupont", "prenom": "Jean"},
	{"id": 2, "nom": "Durand", "prenom": "Marie"},
	{"id": 3, "nom": "Martin", "prenom": "Paul"}
]

def getListProf():
	"""Retourne la liste de tous les professeurs."""
	return tableProf

def CreateProf(nom, prenom):
    """Crée un nouveau professeur et l'ajoute à la tableProf."""
    new_id = max(prof["id"] for prof in tableProf) + 1
    new_prof = {"id": new_id, "nom": nom, "prenom": prenom}
    tableProf.append(new_prof)
    return new_prof

def UpdateProf(prof_id, nom=None, prenom=None):
    """Met à jour les informations d'un professeur existant."""
    for prof in tableProf:
        if prof["id"] == prof_id:
            if nom is not None:
                prof["nom"] = nom
            if prenom is not None:
                prof["prenom"] = prenom
            return prof
    return None  # Retourne None si le professeur n'est pas trouvé

def deleteProf(prof_id):
    """Supprime un professeur de la tableProf."""
    global tableProf
    tableProf = [prof for prof in tableProf if prof["id"] != prof_id]
    return {"message": f"Professeur avec id {prof_id} supprimé."}