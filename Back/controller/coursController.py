import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parents[1] / "Base" / "database.db"

def get_conn():
    conn = sqlite3.connect(str(DB_PATH), check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

def getListCours():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM cours")
    rows = [dict(row) for row in cur.fetchall()]
    conn.close()
    return rows

def CreateCours(matiere, date_debut, date_fin, duree_total, id_promo, id_salle, id_prof):
    conn = get_conn()
    cur = conn.cursor()
    # On insère toutes les informations, y compris les fameux IDs
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
