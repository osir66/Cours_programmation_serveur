

from fastapi import APIRouter
from pydantic import BaseModel
from Back.controller import userController

router = APIRouter(prefix="/user")

# Endpoint pour récupérer un utilisateur par id
@router.get("/getUser")
def get_user(id_user: int):
    return userController.GetUser(id_user)

@router.get("/getListUser")
def get_list_user():
	return userController.getListUser()


class UserCreate(BaseModel):
    nom: str
    email: str
    password: str
    admin: bool

@router.post("/create")
def create_user(user: UserCreate):
    return userController.CreateUser(user.nom, user.email, user.password, user.admin)


class UserUpdate(BaseModel):
    id_user: int
    nom: str
    email: str
    password: str
    admin: bool

@router.put("/updateUser")
def update_user(user: UserUpdate):
    return userController.UpdateUser(user.id_user, user.nom, user.email, user.password, user.admin)
