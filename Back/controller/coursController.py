import sqlite3
from pathlib import Path

#définit le chemin vers la base de données
DB_PATH = Path(__file__).resolve().parents[1] / "Base" / "database.db"

#foncton pour une connexion à la base de données 
def get_conn():
    conn = sqlite3.connect(str(DB_PATH), check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

#fonction pour récupérer la liste des cours
def getListCours():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM cours")
    rows = [dict(row) for row in cur.fetchall()]
    conn.close()
    return rows

#fonction pour créer un cours
def CreateCours(matiere, date_debut, date_fin, duree_total, id_promo, id_salle, id_prof):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO cours (matiere, date_debut, date_fin, duree_total, id_promo, id_salle, id_prof) 
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (matiere, date_debut, date_fin, duree_total, id_promo, id_salle, id_prof))
    
    conn.commit()
    new_id = cur.lastrowid
    conn.close()
    
    return {
        "id_cours": new_id, 
        "matiere": matiere, 
        "date_debut": date_debut, 
        "date_fin": date_fin,
        "duree_total": duree_total,
        "id_promo": id_promo,
        "id_salle": id_salle,
        "id_prof": id_prof,
    }	
 #fonction pour mettre à jour un cours
def updateCours(id_cours, matiere=None, date_debut=None, date_fin=None, duree_total=None, id_promo=None, id_salle=None, id_prof=None):
    conn = get_conn()
    cur = conn.cursor()
    
    updates = []
    params = []
    
    if matiere:
        updates.append("matiere = ?")
        params.append(matiere)
    if date_debut:
        updates.append("date_debut = ?")
        params.append(date_debut)
    if date_fin:
        updates.append("date_fin = ?")
        params.append(date_fin)
    if duree_total:
        updates.append("duree_total = ?")
        params.append(duree_total)
    if id_promo:
        updates.append("id_promo = ?")
        params.append(id_promo)
    if id_salle:
        updates.append("id_salle = ?")
        params.append(id_salle)
    if id_prof:
        updates.append("id_prof = ?")
        params.append(id_prof)

    if not updates:
        conn.close()
        return {"message": "Rien à mettre à jour"}
        
    params.append(id_cours)
    cur.execute(f"UPDATE cours SET {', '.join(updates)} WHERE id_cours = ?", params)
    
    conn.commit()
    conn.close()
    
    return {"message": f"Cours {id_cours} mis à jour avec succès"}

#foction pour supprimer un cours
def deleteCours(id_cours):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("DELETE FROM cours WHERE id_cours = ?", (id_cours,))
    conn.commit()
    conn.close()
    return {"message": f"Cours {id_cours} supprimé avec succès"}
