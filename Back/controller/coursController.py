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
