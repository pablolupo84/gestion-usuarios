#Utilizo una imagen base de Python 3.12

FROM python:3.12-slim
LABEL description = "Imagen de gestion-usuarios"

#Asigno como directorio de trabajo /app
WORKDIR /app/usuarios

COPY ./usuarios /app/usuarios/

RUN pip install --no-cache-dir -r /app/usuarios/requirements.txt

RUN mkdir -p /app/logs

EXPOSE 8000

CMD ["uvicorn", "main_user:app", "--reload" ,"--host", "0.0.0.0", "--port", "8000"]
