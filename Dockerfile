#Buscando una imagen que contenga Python y FastAPI me encontre con esto

FROM python:3.9-slim
LABEL Description = "Imagen de gestion-usuarios"

WORKDIR /app
COPY ./ ./

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--reload" ,"--host", "0.0.0.0", "--port", "8000"]

#docker build -t gestion-usuarios .
#docker run -d --name my-container-gestion-usuarios -p 8000:8000 gestion-usuarios
