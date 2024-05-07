from fastapi import FastAPI,HTTPException,Depends,Header
from login import Login
from datetime import timedelta,datetime
from jose import jwt
import os

#Variables de entorno
var_access_token = int(os.environ.get("ACCESS_TOKEN_EXPIRACION_MIN"))
var_secret_key = os.environ.get("SECRET_KEY")
var_algorithm = os.environ.get("ALGORITHM")

app=FastAPI()

@app.get("/")
async def root():
    return {"message" : "Esta es la app para Gestion de Login - Pablo Lupo"}

#usuarios registrados en el sistema con nombre y contraseña.
listado_usuarios = [
    Login(nombre="pepeLuis",contraseña="12345"),
    Login(nombre="mariaElena",contraseña="admin1234"),
    Login(nombre="coquiArgento",contraseña="admin")]

#Funcion Auxiliar - Verificacion de usuario en mi listado de usuarios
def verificar_usuario(nombre:str,contraseña:str):
    for data in listado_usuarios:
        if nombre==data.nombre and contraseña==data.contraseña:
            return data
    return None          

#Funcion Auxiliar - CReacion de access tocke con tiempo por defecto de 10 minutos
def crear_access_token(datos:dict,expires_delta:timedelta=None):
    datos_copiar=datos.copy()
    if expires_delta:
        expire=datetime.now()+expires_delta
    else:
        expire=datetime.now()+ timedelta(minutes=var_access_token)
    datos_copiar.update({"exp":expire})
    token=jwt.encode(datos_copiar,key=var_secret_key,algorithm=var_algorithm)
    return token

#Endpoint para Login de un usuario
@app.post("/login")
def login(datos:Login):
    datos_usuario=verificar_usuario(datos.nombre,datos.contraseña)
    if datos_usuario:
        access_token_expires = timedelta (minutes=var_access_token)
        access_token_jwt=crear_access_token({"sub": datos_usuario.nombre},access_token_expires)
        return {"access_token" : access_token_jwt,
                "token_type":"bearer"}       
    raise HTTPException(status_code=401, detail="Credenciales Invaldia")

#Funcion Auxiliar para saber si un token es valido
def es_token_valido(token:str):
    try:
        decodificacion=jwt.decode(token,var_secret_key,algorithms=[var_algorithm])
        return decodificacion #{'sub': 'pepeLuis', 'exp': 1714856803}
    except jwt.JWTError:
        #print (jwt.JWTError.description)
        return None

#Funcion Auxiliar para saber si un token esta expirado
def esta_expirado_token(token:str):
    decodificacion=jwt.decode(token,var_secret_key,algorithms=[var_algorithm])
    tiempo_expiracion=datetime.fromtimestamp(decodificacion['exp'])
    return datetime.now()>=tiempo_expiracion

#Funcion Auxiliar para obtener un usuario a partir de un token
def obtener_usuario_desde_token(token:str):
    try:
        decodificacion=jwt.decode(token,var_secret_key,algorithms=[var_algorithm])
        return decodificacion.get("sub") #{'sub': 'pepeLuis', 'exp': 1714856803}
    except jwt.JWTError:
        return None
    
#Funcion Auxiliar para VERIFICAR Y VALIDAR Un token
def verificar_token(token:str):
    if es_token_valido(token):
        if esta_expirado_token(token):
            raise HTTPException(status_code=401, detail="Token expirado")
        else:
            return obtener_usuario_desde_token(token)
    else:
        raise HTTPException(status_code=401, detail="Token invalido")

#Endpoint para una ruta protegida
@app.get("/obtener_usuario_actual")
def ruta_solo_para_autenticados(usuario_autenticado: str = Depends(verificar_token)):
    return{"mensaje":"Esta ruta es solo para usuarios autenticados: " + usuario_autenticado}

#Endpoint para Logout de un usuario
@app.post("/logout")
def login(datos:Login):
    #Decidi dejarlo que por su naturaleza se invalide el token por el tiempo de expiracion configurado
    return{"message":"Logout"}

