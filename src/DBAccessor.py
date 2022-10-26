from RequestModel import *
import pymongo
from bson.objectid import ObjectId

db_client = pymongo.MongoClient("mongodb+srv://bharat19461:bharatsoni@cluster0.eruaidg.mongodb.net/?retryWrites=true&w=majority")
current_db = db_client["currentdb"]
user_db=current_db["userdb"]


def add_user(user:UserRequestModel)->dict:
    user_id=user_db.insert_one(user.__dict__).inserted_id
    return user_db.find_one(user_id)


def get_user(id:str)->dict:
    return user_db.find_one({"_id":ObjectId(id)})


def update_user(id:str,user:UserRequestModel)->dict:
    user_db.update_one({"_id":ObjectId(id)},{"$set":user.__dict__})
    return user_db.find_one(ObjectId(id))


def delete_user(id:str)->dict:
    user=user_db.find_one({"_id":ObjectId(id)})
    user_db.delete_one({"_id":ObjectId(id)})
    return user


def get_all_users()->list[dict]:
    return [x for x in user_db.find({})]


def delete_all_users()->list[dict]:
    all_user=get_all_users()
    user_db.delete_many({})
    return all_user