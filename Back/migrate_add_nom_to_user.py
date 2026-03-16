import sqlite3
from pathlib import Path

# Chemin vers la base de données (toujours relatif à la racine du projet)
project_root = Path(__file__).resolve().parents[1]
db_path = project_root / "Back" / "Base" / "database.db"

conn = sqlite3.connect(str(db_path))
cur = conn.cursor()

try:
    cur.execute("ALTER TABLE USER ADD COLUMN nom TEXT;")
    print("Colonne 'nom' ajoutée à USER.")
except sqlite3.OperationalError as e:
    if "duplicate column name" in str(e):
        print("La colonne 'nom' existe déjà.")
    else:
        print("Erreur:", e)
finally:
    conn.commit()
    cur.close()
    conn.close()
