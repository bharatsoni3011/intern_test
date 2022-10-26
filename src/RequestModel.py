from pydantic import BaseModel

class UserRequestModel(BaseModel):
    name:str=""
    mobile:str=""
