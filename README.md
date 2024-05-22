# gestion-usuarios v1

Trabajo Practico Inicial - Gestion de Usuarios con FAST API PABLO LUPO

3 carpetas con sus codigos fuentes
#autenticacion
#usuarios
#tests

1 carpeta de logs

Para correr la app se necesita realizar lo siguiente:

-Tener instalado Docker 26.0.1
-Realizar un clone del respositorio: 
    git clone https://github.com/pablolupo84/gestion-usuarios.git
-Sobre el directorio raiz: 
    cd gestion-usuarios
    docker compose up

#usuarios
http://localhost:8000/

#autenticacion
http://localhost:8001/

Se generan pruebas automatizadas con pytest para las autenticaciones.

Para Realizar las Pruebas en Postman, hay una coleccion en:
test/TP-Usuarios.postman_collection.json

Para todas las pruebas en que se necesita realizar una verificacion, hay que insertar un token valido.