import sqlite3
from pathlib import Path

# Pointe vers Back/Base/database.db
DB_PATH = Path(__file__).resolve().parents[1] / "Base" / "database.db"

#fonction pour la connexion à la base de données
def get_conn():
    conn = sqlite3.connect(str(DB_PATH), check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

#fonction pour récupérer la liste des salles
def getListSalles():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id_salle AS id, nom_salle, capacite FROM salle")
    rows = [dict(row) for row in cur.fetchall()]
    conn.close()
    return rows

#fonction pour créer les salles 
def CreateSalle(nom_salle, capacite):
    conn = get_conn()
    cur = conn.cursor()
    # On met à jour la requête SQL
    cur.execute("INSERT INTO salle (nom_salle, capacite) VALUES (?, ?)", (nom_salle, capacite))
    conn.commit()
    new_id = cur.lastrowid
    conn.close()
    return {"id": new_id, "nom_salle": nom_salle, "capacite": capacite}