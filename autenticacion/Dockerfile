#Utilizo una imagen base de Python 3.12

FROM python:3.12-slim
LABEL description = "Imagen para Autenticacion"

#Asigno como directorio de trabajo /app
WORKDIR /app/autenticacion

COPY ./autenticacion /app/autenticacion/

RUN pip install --no-cache-dir -r /app/autenticacion/requirements.txt

EXPOSE 8001

CMD ["uvicorn", "main:app", "--reload" ,"--host", "0.0.0.0", "--port", "8001"]
