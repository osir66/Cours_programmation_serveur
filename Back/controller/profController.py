import sqlite3
from pathlib import Path

# Pointe vers Back/Base/database.db
DB_PATH = Path(__file__).resolve().parents[1] / "Base" / "database.db"

# Fonction pour une connexion à la base de données 
def get_conn():
    conn = sqlite3.connect(str(DB_PATH), check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

# Fonction qui récupère la liste des profs
def getListProf():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id_prof AS id, nom, prenom FROM prof")
    rows = [dict(row) for row in cur.fetchall()]
    conn.close()
    return rows

# Fonction pour créer un prof 
def CreateProf(nom, prenom):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("INSERT INTO prof (nom, prenom) VALUES (?, ?)", (nom, prenom))
    conn.commit()
    new_id = cur.lastrowid
    conn.close()
    return {"id": new_id, "nom": nom, "prenom": prenom}

# Fonction pour changer les donées d'un prof 
def UpdateProf(prof_id, nom=None, prenom=None):
    conn = get_conn()
    cur = conn.cursor()
    updates = []
    params = []
    if nom:
        updates.append("nom = ?")
        params.append(nom)
    if prenom:
        updates.append("prenom = ?")
        params.append(prenom)

    if not updates:
        conn.close()
        return {"message": "Rien à mettre à jour"}
        
    params.append(prof_id)
    query = f"UPDATE prof SET {', '.join(updates)} WHERE id_prof = ?"
    cur.execute(query, params)  
    conn.commit()
    conn.close()
    return {"message": f"Professeur {prof_id} mis à jour avec succès"}

# fonction pour supprimer un prof
def deleteProf(prof_id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("DELETE FROM prof WHERE id_prof = ?", (prof_id,))
    conn.commit()
    conn.close()
    return {"message": f"Professeur {prof_id} supprimé avec succès"}