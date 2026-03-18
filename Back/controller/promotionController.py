import sqlite3
from pathlib import Path

# Pointe vers Back/Base/database.db
DB_PATH = Path(__file__).resolve().parents[1] / "Base" / "database.db"

#fonction pour la connexion à la base de données 
def get_conn():
    conn = sqlite3.connect(str(DB_PATH), check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

#fonction pour récupérer la liste des promotions
def getListPromotions():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id_promo AS id, nom_promotion, annee FROM promotion")
    rows = [dict(row) for row in cur.fetchall()]
    conn.close()
    return rows

#fonction pour créer une promotion
def CreatePromotion(nom_promotion, annee):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("INSERT INTO promotion (nom_promotion, annee) VALUES (?, ?)", (nom_promotion, annee))
    conn.commit()
    new_id = cur.lastrowid
    conn.close()
    return {"id": new_id, "nom_promotion": nom_promotion, "annee": annee}