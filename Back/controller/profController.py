import sqlite3
from pathlib import Path

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
    cur.close()
    conn.close()
    return rows

def CreateProf(nom, prenom):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("INSERT INTO prof (nom, prenom) VALUES (?, ?)", (nom, prenom))
    conn.commit()
    new_id = cur.lastrowid
    cur.close()
    conn.close()
    return {"id": new_id, "nom": nom, "prenom": prenom}

def UpdateProf(prof_id, nom=None, prenom=None):
    conn = get_conn()
    cur = conn.cursor()
    # construire dynamiquement les champs à mettre à jour
    updates = []
    params = []
    if nom is not None:
        updates.append("nom = ?"); params.append(nom)
    if prenom is not None:
        updates.append("prenom = ?"); params.append(prenom)
    if not updates:
        cur.close(); conn.close(); return {"message": "Rien à mettre à jour"}
    params.append(prof_id)
    cur.execute(f"UPDATE prof SET {', '.join(updates)} WHERE id_prof = ?", params)
    conn.commit()
    cur.execute("SELECT id_prof AS id, nom, prenom FROM prof WHERE id_prof = ?", (prof_id,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    return dict(row) if row else {"message": f"Professeur {prof_id} non trouvé.", "status": 404}

def deleteProf(prof_id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("DELETE FROM prof WHERE id_prof = ?", (prof_id,))
    conn.commit()
    cur.close()
    conn.close()
    return {"message": f"Professeur avec id {prof_id} supprimé."}