from pydantic import BaseModel

class Login(BaseModel):    
        nombre:str
        contraseña:str