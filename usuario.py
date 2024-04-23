import datetime

class Usuario:
    def __init__(self,identificador,roles,fecha_creacion,fecha_eliminacion,nombre):
        self.identificador=identificador
        self.roles=roles
        self.fecha_creacion=fecha_creacion
        self.fecha_eliminacion=fecha_eliminacion
        self.nombre=nombre
        