from fastapi import APIRouter
from Back.controller import userController

router = APIRouter()

@router.get("/getListUser")
def get_list_user():
	return userController.getListUser()

@router.post("/addUser")
def add_user(id_user : int ,email : str,password : str ,admin : bool):
    return userController.CreateUser(id_user, email, password, admin)

@router.get("/updateUser")
def update_user(id_user : int ,email : str,password : str ,admin : bool):
      return userController.UpdateUser(id_user, email, password, admin)
