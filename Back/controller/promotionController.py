import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parents[1] / "Base" / "database.db"

def get_conn():
    conn = sqlite3.connect(str(DB_PATH), check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

def getListPromotions():
    conn = get_conn()
    cur = conn.cursor()
    # On utilise id_promo, nom_promotion et annee
    cur.execute("SELECT id_promo AS id, nom_promotion, annee FROM promotion")
    rows = [dict(row) for row in cur.fetchall()]
    conn.close()
    return rows

def CreatePromotion(nom_promotion, annee):
    conn = get_conn()
    cur = conn.cursor()
    # On met à jour la requête SQL
    cur.execute("INSERT INTO promotion (nom_promotion, annee) VALUES (?, ?)", (nom_promotion, annee))
    conn.commit()
    new_id = cur.lastrowid
    conn.close()
    return {"id": new_id, "nom_promotion": nom_promotion, "annee": annee}