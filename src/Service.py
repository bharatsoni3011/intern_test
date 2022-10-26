from RequestModel import UserRequestModel
from DTO import *
import DBAccessor

def dict_to_user(user:dict)->UserModel:
    try:
        return UserModel(id=str(user['_id']),name=user['name'],mobile=user["mobile"])
    except:
        return "ERROR_NOT_KNOWN"


def add_user(user:UserRequestModel) -> UserModel:
    response=DBAccessor.add_user(user)
    if not isinstance(response,dict):
        return "ERROR_USER_NOT_ADDED"
    return dict_to_user(response)


def get_user(id:str) -> UserModel:
    response=DBAccessor.get_user(id)
    if not isinstance(response,dict):
        return "ERROR_FETCHING_USER"
    return dict_to_user(response)


def update_user(id:str,user:UserRequestModel) -> UserModel:
    response=get_user(id)
    if not isinstance(response,UserModel):
        return response
    
    updated_response=DBAccessor.update_user(id,user)
    if not isinstance(updated_response,dict):
        return "ERROR_USER_NOT_UPDATED"
    return dict_to_user(updated_response)


def delete_user(id:str) -> UserModel:
    response=DBAccessor.delete_user(id)
    if not isinstance(response,dict):
        return "ERROR_USER_NOT_DELETED"
    return dict_to_user(response)


def get_all_users()->list[UserModel]:
    response=DBAccessor.get_all_users()
    if not isinstance(response,list):
        return "ERROR_FETCHING_USER"
    return list(map(dict_to_user,response))


def delete_all_users()->list[UserModel]:
    response=DBAccessor.delete_all_users()
    if not isinstance(response,list):
        return "ERROR_USER_NOT_DELETED"
    return list(map(dict_to_user,response))
