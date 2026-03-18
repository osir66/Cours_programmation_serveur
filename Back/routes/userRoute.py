from fastapi import APIRouter
from Back.controller import userController


router = APIRouter()

#route pour récupérer la liste de tous les utilisateurs
@router.get("/getListUser")
def get_list_user():
    return userController.getListUser()

#route pour ajouter un utilisateur
@router.post("/addUser")
def add_user(id_user: int, email: str, password: str, admin: bool):
    return userController.CreateUser(id_user, email, password, admin)

#route pour modifier un utilisateur
@router.get("/updateUser")
def update_user(id_user: int, email: str, password: str, admin: bool):
    return userController.UpdateUser(id_user, email, password, admin)

#route pour supprimer un utilisateur
@router.delete("/deleteUser/{id_user}")
def delete_user(id_user: int):
    return userController.deleteUser(id_user)
