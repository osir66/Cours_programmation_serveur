tableCours = [
	{"id_cours": 1, "matière": "Mathématiques", "prof_id": 1, "durée": 2, "id_salle": 101, "date_heure": "2024-09-01", "id_promo": 1},
	{"id_cours": 2, "matière": "Physique", "prof_id": 2, "durée": 3, "id_salle": 102, "date_heure": "2024-09-02", "id_promo": 1},
	{"id_cours": 3, "matière": "Chimie", "prof_id": 3, "durée": 2, "id_salle": 103, "date_heure": "2024-09-03", "id_promo": 1}
]

def getListCours():
	"""Retourne la liste de tous les cours."""
	return tableCours

def CreateCours(matière, prof_id, durée, id_salle, date_heure, id_promo):
	"""Crée un nouveau cours et l'ajoute à la tableCours."""
	new_id = max(cours["id_cours"] for cours in tableCours) + 1
	new_cours = {
		"id_cours": new_id,
		"matière": matière,
		"prof_id": prof_id,
		"durée": durée,
		"id_salle": id_salle,
		"date_heure": date_heure,
		"id_promo": id_promo
	}
	tableCours.append(new_cours)
	return new_cours

def UpdateCours(cours_id, matière=None, prof_id=None, durée=None, id_salle=None, date_heure=None, id_promo=None):
	"""Met à jour les informations d'un cours existant."""
	for cours in tableCours:
		if cours["id_cours"] == cours_id:
			if matière is not None:
				cours["matière"] = matière
			if prof_id is not None:
				cours["prof_id"] = prof_id
			if durée is not None:
				cours["durée"] = durée
			if id_salle is not None:
				cours["id_salle"] = id_salle
			if date_heure is not None:
				cours["date_heure"] = date_heure
			if id_promo is not None:
				cours["id_promo"] = id_promo
			return cours
	return {"message": f"Cours avec id {cours_id} non trouvé.", "status": 404} 

def deleteCours(cours_id):
	"""Supprime un cours de la tableCours."""
	global tableCours
	tableCours = [cours for cours in tableCours if cours["id_cours"] != cours_id]
	return {"message": f"Cours avec id {cours_id} supprimé.", "status": 200}	

