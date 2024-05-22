#Utilizo una imagen base de Python 3.12

FROM python:3.12-slim
LABEL description = "Imagen para Test"

#Asigno como directorio de trabajo /app
WORKDIR /app/tests

COPY . /app
#COPY /tests/test_usuarios.py /app/usuarios
#COPY /tests/test_autenticacion.py /app/autenticacion
#COPY /tests/script-bash.sh /app/

COPY autenticacion/main_auth.py /app/tests
COPY autenticacion/login.py /app/tests
COPY usuarios/main_user.py /app/tests
COPY usuarios/usuario.py /app/tests

RUN pip install --no-cache-dir -r /app/tests/requirements.txt
    
RUN chmod +x /app/tests/script-bash.sh

#CMD ["pytest","-v"]
#CMD ["tail","-f","/dev/null"]
CMD ["/app/tests/script-bash.sh"]