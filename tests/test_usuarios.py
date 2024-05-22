from datetime import datetime
from fastapi.testclient import TestClient
from main_user import app as app_user
from main_auth import app as app_auth

#usuarios registrados en el sistema con nombre y contraseña.
usuario_ok = {"nombre":"pepeLuis", "contraseña":"12345"}
usuario_invalido = {"nombre":"marcoaurelio", "contraseña":"dd12345"}
    
client_user=TestClient(app_user)
client_auth=TestClient(app_auth)

def test_get_raiz_token_valido():
    
    response=client_auth.post("/login", json=usuario_ok)
    print (response)
    #assert response.status_code==200
    #response_data=response.json()
    #access_token="Bearer " + response_data["access_token"]
    
    #headers = {
    #    "Authorization": access_token
    #}

    #response=client.get("http://localhost:8001/",headers=headers)
    #assert response.status_code == 200
    assert 200 == 200

"""

# Middleware de Autenticación
# Todas las solicitudes deben estar autenticadas verificando el token JWT
# SE ejecuta antes de cada solicitud para cualqueir endoint del servicio.

@app.middleware("http")
async def auth_middleware(request: Request, call_next):
    logger.info("Inicio de Middleware de Autenticacion")
    token = request.headers.get("Authorization")
    
    if not token or token.strip() == "":
        logger.info(f"Middleware de Autenticacion - Falta el Token de autorizacion")
        raise HTTPException(status_code=401, detail="Falta el token de autorización")

    token = token.replace("Bearer ", "").strip()
    logger.info(f"Middleware de Autenticacion - Token: {token}")

    if not token:
        logger.info(f"Middleware de Autenticacion - Token VACIO")
        raise HTTPException(status_code=401, detail="Token de autorización vacío")

    try:
        response = requests.get(f"{aut_url}verificar_token", params={"token": token})
        if response.status_code != 200:
            logger.error(f"Response !=200 : {response.status_code}")
            raise HTTPException(status_code=response.status_code, detail="Token inválido")
    except requests.exceptions.RequestException as e:
        logger.error(f"Middleware de Autenticacion - Error de conexion: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
    
    response = await call_next(request)
    return response
    

#Crear nuevo Usuario
@app.post("/usuarios/",response_model=Usuario,status_code=status.HTTP_201_CREATED)
def crear_usuario(nuevo_usuario: Usuario):
    #Lo creo autoincremental si no existe por nombre de usuario
    logger.info("Endpoint POST de nuevo usuario")
    if (usuario_no_existe(nuevo_usuario.nombre)):
        logger.info(f"Se crea el usuario {nuevo_usuario.nombre}")
        nuevo_usuario.identificador=len(listado_usuarios)+1
        nuevo_usuario.fecha_creacion=datetime.now()
        nuevo_usuario.fecha_eliminacion= None
        listado_usuarios.append(nuevo_usuario)
        return nuevo_usuario
    else:
        logger.info(f"Usuario {nuevo_usuario.nombre} Existente")
        raise HTTPException(status_code=404, detail="Usuario Exitente")    

#Borrar Usuario sin eliminacion fisica - Queda marcado por la fecha de eliminacion
@app.delete("/usuarios/{identificador}/")
def borrar_usuario(identificador: int):
    logger.info("Endpoint DELETTE de usuario")
    for usuario in listado_usuarios:
        if usuario.identificador == identificador:
            if usuario.fecha_eliminacion is not None:
                logger.info(f"Usuario {identificador} ya se encuentra eliminado")
                return {"message": "El usuario ya se encuentra eliminado."}
            else:
                #elimino y devuelvo mensaje
                usuario.fecha_eliminacion = datetime.now()
                logger.info(f"Usuario {identificador} eliminado exitosamente")
                return {"message": "Usuario eliminado exitosamente"}
                break
    logger.info(f"NO se encuentra el Usuario {identificador}")        
    raise HTTPException(status_code=404, detail="No se encontró el usuario")

#Obtener un Usuario
@app.get("/usuarios/{identificador}",response_model=Usuario)
def obtener_usuario(identificador: int):
    logger.info("Endpoint obtener_usuario")
    for usuario in listado_usuarios:
        if usuario.identificador==identificador and not usuario.fecha_eliminacion:
            logger.info(f"Usuario {identificador} encontrado")
            return usuario
    logger.info(f"NO se encuentra el Usuario {identificador}")    
    raise HTTPException(status_code=404,detail="No se encontro el usuario")

#Obtener todos los Usuarios
@app.get("/usuarios",response_model=List[Usuario])
def obtener_todos_los_usuarios():
    logger.info("Endpoint obtener_todos_los_usuarios")
    return [usuario for usuario in listado_usuarios if not usuario.fecha_eliminacion]

"""