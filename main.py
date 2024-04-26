from fastapi import FastAPI, HTTPException
from datetime import datetime
from usuario import Usuario
from typing import List

app=FastAPI()

#Inicialmente se salva en una lista, luego pienso pasarlo a base de datos.
listado_usuarios:List[Usuario]=[]

@app.get("/")
async def root():
    return {"message" : "Esta es la app para Gestion de Usuarios - Pablo Lupo"}

#Crear nuevo Usuario
@app.post("/usuarios/",response_model=Usuario)
def crear_usuario(nuevo_usuario: Usuario):
    #Lo creo autoincremental
    nuevo_usuario.identificador=len(listado_usuarios)+1
    nuevo_usuario.fecha_creacion=datetime.now()
    nuevo_usuario.fecha_eliminacion= None
    listado_usuarios.append(nuevo_usuario)
    return nuevo_usuario

#Borrar Usuario sin eliminacion fisica - Queda marcado por la fecha de eliminacion
@app.delete("/usuarios/{identificador}/")
def borrar_usuario(identificador: int):
    for usuario in listado_usuarios:
        if usuario.identificador == identificador:
            if usuario.fecha_eliminacion is not None:
                return {"message": "El usuario esta eliminado."}
            else:
                #elimino y devuelvo mensaje
                usuario.fecha_eliminacion = datetime.now()
                return {"message": f"Se elimina el usuario con ID {usuario.identificador} satisfactoriamente."}
    raise HTTPException(status_code=404, detail="No se encontró el usuario")

#Obtener un Usuario
@app.get("/usuarios/{identificador}/",response_model=Usuario)
def obtener_usuario(identificador: int):
    for usuario in listado_usuarios:
        if usuario.identificador==identificador and not usuario.fecha_eliminacion:
            return usuario
    raise HTTPException(status_code=404,detail="No se encontro el usuario")

#Obtener todos los Usuarios
@app.get("/usuarios/",response_model=List[Usuario])
def obtener_todos_los_usuarios():
    return [usuario for usuario in listado_usuarios if not usuario.fecha_eliminacion]
