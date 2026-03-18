import sqlite3
from pathlib import Path

# Pointe vers Back/Base/database.db
DB_PATH = Path(__file__).resolve().parents[1] / "Base" / "database.db"

# Fonction pour la connexion à la base de données
def get_conn():
    conn = sqlite3.connect(str(DB_PATH), check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

# Fonction pour récupérer la liste des salles
def getListSalles():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id_salle AS id, nom_salle, capacite FROM salle")
    rows = [dict(row) for row in cur.fetchall()]
    conn.close()
    return rows

# Fonction pour créer les salles
def CreateSalle(nom_salle, capacite):
    conn = get_conn()
    cur = conn.cursor()
    # On met à jour la requête SQL
    cur.execute("INSERT INTO salle (nom_salle, capacite) VALUES (?, ?)", (nom_salle, capacite))
    conn.commit()
    new_id = cur.lastrowid
    conn.close()
    return {"id": new_id, "nom_salle": nom_salle, "capacite": capacite}

# Fonction pour modifier les salles
def updateSalle(salle_id, nom_salle=None, capacite=None):
    conn = get_conn()
    cur = conn.cursor()
    updates = []
    params = []
    if nom_salle:
        updates.append("nom_salle = ?")
        params.append(nom_salle)
    if capacite:
        updates.append("capacite = ?")
        params.append(capacite)

    if not updates:
        conn.close()
        return {"message": "Rien à mettre à jour"}
        
    params.append(salle_id)
    cur.execute(f"UPDATE salle SET {', '.join(updates)} WHERE id_salle = ?", params)
    conn.commit()
    conn.close()
    return {"message": f"Salle {salle_id} mise à jour avec succès"}

# Fonction pour supprimer une salle
def deleteSalle(salle_id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("DELETE FROM salle WHERE id_salle = ?", (salle_id,))
    conn.commit()
    conn.close()
    return {"message": f"Salle {salle_id} supprimée avec succès"}