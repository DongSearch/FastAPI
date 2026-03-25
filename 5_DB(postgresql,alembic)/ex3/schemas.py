from pydantic import BaseModel

class UserCreate(BaseModel):
    name : str
    content : str

class UserResponse(BaseModel): #DTO
    name : str
    content : str
    id : int
# we can't read object, ORM can be read like dictionary
# Sqlalchemy -> return object, Pydantic change it to json
    class Config : 
        from_attributes = True