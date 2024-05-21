from fastapi import FastAPI,HTTPException,Depends,Header
from login import Login
from datetime import timedelta,datetime
from jose import jwt
import os,logging

# Configuración de logging
log_file=os.path.join('/app/logs','app.log')

logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler(log_file),
                    logging.StreamHandler()]
                    )

logger = logging.getLogger(__name__)

#Variables de entorno
var_access_token = int(os.environ.get("ACCESS_TOKEN_EXPIRACION_MIN"))
var_secret_key = os.environ.get("SECRET_KEY")
var_algorithm = os.environ.get("ALGORITHM")

app=FastAPI()

@app.get("/")
async def root():
    logger.info("Endpoint Acceso a la ruta raíz - Autenticacion")
    return {"message" : "Esta es la app para la Autenticacion - Pablo Lupo"}

#usuarios registrados en el sistema con nombre y contraseña.
listado_usuarios = [
    Login(nombre="pepeLuis",contraseña="12345"),
    Login(nombre="mariaElena",contraseña="admin1234"),
    Login(nombre="coquiArgento",contraseña="admin")]

#Funcion Auxiliar - Verificacion de usuario en mi listado de usuarios
def verificar_usuario(nombre:str,contraseña:str):
    logger.info("Ingreso a Funcion Auxiliar verificar_usuario")
    for data in listado_usuarios:
        if nombre==data.nombre and contraseña==data.contraseña:
            logger.info(f"Usuario verificado {nombre}")
            return data
    logger.info("Usuario no verificado o inexistente")
    return None          

#Funcion Auxiliar - CReacion de access token
def crear_access_token(datos:dict,expires_delta:timedelta=None):
    logger.info("Ingreso a Funcion Auxiliar crear_access_token")
    datos_copiar=datos.copy()
    logger.info("Asignacion de tiempo de expiracion")
    if expires_delta:
        expire=datetime.now()+expires_delta
    else:
        expire=datetime.now()+ timedelta(minutes=var_access_token)
    datos_copiar.update({"exp":expire})
    logger.info(f"Asignacion y Actualizacion de tiempo de expiracion = {expire}")
    token=jwt.encode(datos_copiar,key=var_secret_key,algorithm=var_algorithm)
    logger.info(f"Token: = {token}")
    return token

#Endpoint para Login de un usuario
@app.post("/login")
def login(datos:Login):
    logger.info("Ingreso a endpoint login")
    datos_usuario=verificar_usuario(datos.nombre,datos.contraseña)
    if datos_usuario:
        access_token_expires = timedelta (minutes=var_access_token)
        access_token_jwt=crear_access_token({"sub": datos_usuario.nombre},access_token_expires)
        return {"access_token" : access_token_jwt,
                "token_type":"bearer"}
    else:
        logger.warning("Credenciales invalidas para realziar el login")
        raise HTTPException(status_code=401, detail="Credenciales Invaldia")

#Endpoint para Logout de un usuario
@app.post("/logout")
def logout(datos:Login):
    #Tiene configurado el deslogueo automatico
    logger.info("Ingreso a endpoint logout - Automatico luego de x minutos configurados")
    return{"message":"Logout Automatico"}

#Funcion Auxiliar para saber si un token es valido
def es_token_valido(token:str):
    logger.info("Ingreso a Funcion Auxiliar es_token_valido")
    try:
        decodificacion=jwt.decode(token,var_secret_key,algorithms=[var_algorithm])
        logger.info(f"Token valido {decodificacion}")
        return decodificacion #{'sub': 'pepeLuis', 'exp': 1714856803}
    except jwt.JWTError:
        logger.warning(f"Token Invalido: {jwt.JWTError}")
        return None

#Funcion Auxiliar para saber si un token esta expirado
def esta_expirado_token(token:str):
    logger.info("Ingreso a Funcion Auxiliar esta_expirado_token")
    try:
        decodificacion=jwt.decode(token,var_secret_key,algorithms=[var_algorithm])
        logger.info(f"Decodificacion: {decodificacion}")
        tiempo_expiracion=datetime.fromtimestamp(decodificacion['exp'])
        logger.info(f"Tiempo de Expiracion: {tiempo_expiracion}")
        logger.info(f"Esta expirado: {datetime.now()>=tiempo_expiracion}")
        return datetime.now()>=tiempo_expiracion
    except jwt.JWTError:
        logger.warning(f"Error decodificando: {jwt.JWTError}")
        return True


#Funcion Auxiliar para obtener un nombre de usuario a partir de un token
def obtener_nombre_usuario_desde_token(token:str):
    logger.info("Ingreso a Funcion Auxiliar obtener_nombre_usuario_desde_token")
    try:
        decodificacion=jwt.decode(token,var_secret_key,algorithms=[var_algorithm])
        logger.info(f"Usuario: {decodificacion.get("sub")}")
        return decodificacion.get("sub") #{'sub': 'pepeLuis', 'exp': 1714856803}
    except jwt.JWTError:
        logger.info(f"Usuario no encontrado: {jwt.JWTError}")
        return None

#Funcion Auxiliar para obtener un usuario a partir de un token
def obtener_usuario_desde_token(token:str):
    logger.info("Ingreso a Funcion Auxiliar obtener_usuario_desde_token")
    try:
        decodificacion=jwt.decode(token,var_secret_key,algorithms=[var_algorithm])
        logger.info(f"Usuario: {decodificacion}")
        return decodificacion #{'sub': 'pepeLuis', 'exp': 1714856803}
    except jwt.JWTError:
        logger.info(f"Usuario no encontrado: {jwt.JWTError}")
        return None

#Endpoint para verificar un token
@app.get("/verificar_token")
def verificar_token(token:str):
    logger.info("Ingreso a endpoint verificar_token")
    decodificacion=es_token_valido(token)
    if decodificacion:
        if esta_expirado_token(token):
            raise HTTPException(status_code=401, detail="Token expirado")
        else:
            return obtener_usuario_desde_token(token)
    else:
        logger.warning("Decodificacion None - Token INvalido")
        raise HTTPException(status_code=401, detail="Token invalido")    
