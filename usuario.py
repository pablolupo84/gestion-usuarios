from datetime import datetime
from pydantic import BaseModel
from typing import List,Optional

#Utilizo la libreria pydantic ya que no me funcionaba de manera clasica al definir el inicializacdor
#def __init__(self,identificador:int,roles:str,nombre:str,fecha_creacion:datetime,
#               fecha_eliminacion:datetime=None):
#LOs dejo como Optional por que en el cbody cuando hago la peticion eexplota sino. Para
#eso importo Optional de la libreria typing

class Usuario(BaseModel):    
        identificador:Optional[int] = None
        roles:List[str]
        nombre:str
        fecha_creacion:Optional[datetime] = None
        fecha_eliminacion:Optional[datetime] = None