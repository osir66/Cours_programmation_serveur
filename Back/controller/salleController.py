import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parents[1] / "Base" / "database.db"

def get_conn():
    conn = sqlite3.connect(str(DB_PATH), check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

def getListSalles():
    conn = get_conn()
    cur = conn.cursor()
    # On utilise bien id_salle, nom_salle et capacite
    cur.execute("SELECT id_salle AS id, nom_salle, capacite FROM salle")
    rows = [dict(row) for row in cur.fetchall()]
    conn.close()
    return rows

def CreateSalle(nom_salle, capacite):
    conn = get_conn()
    cur = conn.cursor()
    # On met à jour la requête SQL
    cur.execute("INSERT INTO salle (nom_salle, capacite) VALUES (?, ?)", (nom_salle, capacite))
    conn.commit()
    new_id = cur.lastrowid
    conn.close()
    return {"id": new_id, "nom_salle": nom_salle, "capacite": capacite}