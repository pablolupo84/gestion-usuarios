# gestion-usuarios v1

Trabajo Practico Inicial - Gestion de Usuarios con FAST API PABLO LUPO

2 carpetas con sus codigos fuentes
#autenticacion
#usuarios

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

Para Realizar las Pruebas en Postman:

GET usuarios_1: obtiene el usuairo con id=1.
POST crear_usuario: Crea un nuevo usuario.
POST login_pepe: Crea un token para el usuario si no existe (Copiar el Token para utilziar luego).
POST login_pepe_false: No puede crear por que ya existe el usuario.
DEL delete_usuario_1: ELimina el usuario conID=1.
DEL delete_usuario_100_false: No puede eliminar por que no existe el usuario con ID=100.
GET obtener_usuario: OBtiene todos los usuarios no eliminados.
GET info_usuario_actual: Agregando el token copiado anteriormente, valida que existe y luego entrega la informaciond e dicho usuario.