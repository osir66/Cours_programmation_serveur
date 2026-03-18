import sqlite3
from pathlib import Path

#Pointe vers Back/Base/database.db
DB_PATH = Path(__file__).resolve().parents[1] / "Base" / "database.db"


#fonction pour la connexion à la base de données
def get_conn():
    conn = sqlite3.connect(str(DB_PATH), check_same_thread=False)
    conn.row_factory = sqlite3.Row


    return conn

#fonction pour récupérer la liste des utilisateurs
def getListUser():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('''SELECT * FROM USER''')
    rows = [dict(row) for row in cur.fetchall()]
    cur.close()


    conn.close()
    return rows

#fonction pour créer un utilisateur
def CreateUser(id_user,email,password,admin):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('''INSERT INTO USER (id_user,email,password,admin) VALUES(?,?,?,?)''',


                (id_user,email,password,admin))
    rows = [dict(row) for row in cur.fetchall()]
    cur.close()
    conn.close()
    return rows

#fonction pour supprimer un utilisateur
def DeleteUser(id_user):


    conn = get_conn()
    cur = conn.cursor()
    cur.execute('''DELETE FROM prof WHERE id_user = ?''', (id_user,))
    conn.commit()
    cur.close()
    conn.close()

#fonction pour mettre à jour un utilisateur
def UpdateUser(id_user,email,password,admin):


    conn = get_conn()
    cur = conn.cursor()
    cur.execute('''UPDATE user SET email = ?, password = ?, admin = ? WHERE id_user = ?''',id_user,email,password,admin)
    conn.commit()
    cur.close()
    conn.close()