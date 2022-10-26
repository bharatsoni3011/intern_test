import fastapi
from DTO import UserModel
from RequestModel import UserRequestModel
import Service
from enum import Enum

app = fastapi.FastAPI()

class Errors(Enum):
    ERROR_FETCHING_USER=fastapi.HTTPException(status_code=301,detail=f"error while fetching user details")
    ERROR_USER_NOT_ADDED=fastapi.HTTPException(status_code=302,detail=f"error while adding the user")
    ERROR_USER_NOT_UPDATED=fastapi.HTTPException(status_code=303,detail=f"error while updating the user")
    ERROR_USER_NOT_DELETED=fastapi.HTTPException(status_code=304,detail=f"error while deleting the user data")
    ERROR_NOT_KNOWN=fastapi.HTTPException(status_code=305,detail=f"unknown error")


@app.post("/user/add")
async def add_user(user:UserRequestModel) -> UserModel:
    response=Service.add_user(user)
    if isinstance(response,UserModel):
        return response
    return Errors[response].value


@app.get("/user/{id}/get")
async def get_user(id:str) -> UserModel:
    response=Service.get_user(id)
    if isinstance(response,UserModel):
        return response
    return Errors[response].value


@app.put("/user/{id}/update")
async def update_user(id:str,user:UserRequestModel) -> UserModel:
    response=Service.update_user(id,user)
    if isinstance(response,UserModel):
        return response
    return Errors[response].value


@app.delete("/user/{id}/delete")
async def delete_user(id:str)->UserModel:
    response=Service.delete_user(id)
    if isinstance(response,UserModel):
        return response
    return Errors[response].value


@app.delete("/user/delete/all")
async def delete_all_users() -> list[UserModel]:
    response=Service.delete_all_users()
    if isinstance(response,list):
        return response
    return Errors[response].value


@app.get('/user/get/all')
async def get_all_users()->list[UserModel]:
    response=Service.get_all_users()
    if isinstance(response,list):
        return response
    return Errors[response].value

