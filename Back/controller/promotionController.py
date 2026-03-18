import sqlite3
from pathlib import Path

# Pointe vers Back/Base/database.db
DB_PATH = Path(__file__).resolve().parents[1] / "Base" / "database.db"

# Fonction pour la connexion à la base de données 
def get_conn():
    conn = sqlite3.connect(str(DB_PATH), check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

# Fonction pour récupérer la liste des promotions
def getListPromotions():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id_promo AS id, nom_promotion, annee FROM promotion")
    rows = [dict(row) for row in cur.fetchall()]
    conn.close()
    return rows

# Fonction pour créer une promotion
def CreatePromotion(nom_promotion, annee):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("INSERT INTO promotion (nom_promotion, annee) VALUES (?, ?)", (nom_promotion, annee))
    conn.commit()
    new_id = cur.lastrowid
    conn.close()
    return {"id": new_id, "nom_promotion": nom_promotion, "annee": annee}

# Fonction pour modifier une promotion
def updatePromotion(promo_id, nom_promotion=None, annee=None):
    conn = get_conn()
    cur = conn.cursor()
    updates = []
    params = []
    if nom_promotion:
        updates.append("nom_promotion = ?")
        params.append(nom_promotion)
    if annee:
        updates.append("annee = ?")
        params.append(annee)

    if not updates:
        conn.close()
        return {"message": "Rien à mettre à jour"}
        
    params.append(promo_id)
    cur.execute(f"UPDATE promotion SET {', '.join(updates)} WHERE id_promo = ?", params)
    conn.commit()
    conn.close()
    return {"message": f"Promotion {promo_id} mise à jour avec succès"}

# Fonction qui supprime une promotion
def deletePromotion(promo_id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("DELETE FROM promotion WHERE id_promo = ?", (promo_id,))
    conn.commit()
    conn.close()
    return {"message": f"Promotion {promo_id} supprimée avec succès"}