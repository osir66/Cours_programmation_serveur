from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from Back.controller import userController


router = APIRouter()


# Route pour récupérer la liste de tous les utilisateurs
@router.get("/getListUser")
def get_list_user():
    return userController.getListUser()


class UserCreate(BaseModel):
    email: str
    password: str
    admin: bool = False


# Route pour ajouter un utilisateur
@router.post("/addUser")
def add_user(payload: UserCreate):
    existing = [u for u in userController.getListUser() if u.get('email') == payload.email]
    if existing:
        raise HTTPException(status_code=400, detail='Un utilisateur avec cet email existe déjà')
    created = userController.CreateUser(payload.email, payload.password, payload.admin)
    return created


# Route pour modifier un utilisateur
@router.put("/updateUser")
def update_user(id_user: int, email: str, password: str, admin: bool):
    return userController.UpdateUser(id_user, email, password, admin)


# Route pour supprimer un utilisateur
@router.delete("/deleteUser/{id_user}")
def delete_user(id_user: int):
    return userController.deleteUser(id_user)


class LoginRequest(BaseModel):
    username: str
    password: str


@router.post('/login')
def login(payload: LoginRequest):
    user = userController.authenticate_user(payload.username, payload.password)
    if not user:
        raise HTTPException(status_code=401, detail='Identifiants invalides')
    return user
