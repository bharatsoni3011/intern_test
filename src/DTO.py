from pydantic import BaseModel

class UserModel(BaseModel):
    id:str|None=None
    name:str=""
    mobile:str=""
