#tout les fonction d'appel du back dans ce fichier
import requests

response = requests.get("http://localhost:8000/professeurs")
if response.status_code == 200:
    professeurs = response.json()
    print(professeurs)