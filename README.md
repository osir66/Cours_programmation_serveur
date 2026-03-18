# Cours_programmation_serveur
Projet dans le cadre du cours de programmation coté serveur, le but est d'utiliser des API et une base donnée

installer :
    FastApi
    Uvicorn
    
Pour lancer le code dans le terminal 
    cd Back 
    uvicorn api:app --reload

pytest ; python -m pytest 

Coverage :  coverage run -m pytest
            coverage report -m

Bandit : bandit -r Back/

flake : flake8 Back/  