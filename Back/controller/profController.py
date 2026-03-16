import sqlite3
from pathlib import Path

# Pointe vers Back/Base/database.db
DB_PATH = Path(__file__).resolve().parents[1] / "Base" / "database.db"

def get_conn():
    conn = sqlite3.connect(str(DB_PATH), check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

def getListProf():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id_prof AS id, nom, prenom FROM prof")
    rows = [dict(row) for row in cur.fetchall()]
    conn.close()
    return rows

def CreateProf(nom, prenom):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("INSERT INTO prof (nom, prenom) VALUES (?, ?)", (nom, prenom))
    conn.commit()
    new_id = cur.lastrowid
    conn.close()
    return {"id": new_id, "nom": nom, "prenom": prenom}

def UpdateProf(prof_id, nom=None, prenom=None):
    conn = get_conn()
    cur = conn.cursor()
    updates = []
    params = []
    if nom:
        updates.append("nom = ?"); params.append(nom)
    if prenom:
        updates.append("prenom = ?"); params.append(prenom)
    
    if not updates:
        conn.close()
        return {"message": "Rien à mettre à jour"}
        
    params.append(prof_id)
    cur.execute(f"UPDATE prof SET {', '.join(updates)} WHERE id_prof = ?", params)
    conn.commit()
    conn.close()
    return {"message": f"Professeur {prof_id} mis à jour avec succès"}