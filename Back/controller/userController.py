import sqlite3
from pathlib import Path

# Pointe vers Back/Base/database.db
DB_PATH = Path(__file__).resolve().parents[1] / "Base" / "database.db"


# Fonction pour la connexion à la base de données
def get_conn():
    conn = sqlite3.connect(str(DB_PATH), check_same_thread=False)
    conn.row_factory = sqlite3.Row


    return conn

# Fonction pour récupérer la liste des utilisateurs
def getListUser():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('''SELECT * FROM USER''')
    rows = [dict(row) for row in cur.fetchall()]
    cur.close()


    conn.close()
    return rows

# Fonction pour créer un utilisateur
def CreateUser(email, password, admin=False):
    conn = get_conn()
    cur = conn.cursor()
    # Insère sans fournir id_user pour laisser SQLite auto-incrémenter
    cur.execute('''INSERT INTO USER (email,password,admin) VALUES(?,?,?)''',
                (email, password, int(bool(admin))))
    conn.commit()
    new_id = cur.lastrowid
    # Retourner l'utilisateur créé
    cur.execute('SELECT id_user, email, admin FROM USER WHERE id_user = ?', (new_id,))
    row = cur.fetchone()
    result = dict(row) if row is not None else None
    cur.close()
    conn.close()
    return result

# Fonction pour supprimer un utilisateur
def DeleteUser(id_user):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('''DELETE FROM USER WHERE id_user = ?''', (id_user,))
    conn.commit()
    cur.close()
    conn.close()

# Fonction pour mettre à jour un utilisateur
def UpdateUser(id_user,email,password,admin):


    conn = get_conn()
    cur = conn.cursor()
    cur.execute('''UPDATE user SET email = ?, password = ?, admin = ? WHERE id_user = ?''',(email,password,admin,id_user))
    conn.commit()
    cur.close()
    conn.close()


def authenticate_user(username: str, password: str):
        conn = get_conn()
        cur = conn.cursor()
        cur.execute('SELECT id_user, email, admin FROM USER WHERE email = ? AND password = ?', (username, password))
        row = cur.fetchone()
        cur.close()
        conn.close()
        if row:
            r = dict(row)
            return {'username': r.get('email'), 'displayName': r.get('email'), 'id_user': r.get('id_user'), 'admin': bool(r.get('admin'))}
        # Comptes en dur pour test rapide
        CREDENTIALS = {
            'user': {'password': 'user', 'displayName': 'User'},
            'admin': {'password': 'admin', 'displayName': 'Admin'}
        }

        entry = CREDENTIALS.get(username)
        if entry and entry.get('password') == password:
            return {'username': username, 'displayName': entry.get('displayName')}
        return None