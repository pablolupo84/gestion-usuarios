#Utilizo una imagen base de Python 3.12
FROM python:3.12-slim
LABEL description = "Imagen de gestion-usuarios"

#Asigno como directorio de trabajo /app
WORKDIR /app

COPY ./ ./

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--reload" ,"--host", "0.0.0.0", "--port", "8000"]

#docker build -t gestion-usuarios .
#docker run -d --name my-container-gestion-usuarios -p 8000:8000 gestion-usuarios
