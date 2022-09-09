# Pre requisitos

- Haber instalado REDIS
-- Instalar para MAC https://redis.io/docs/getting-started/installation/install-redis-on-mac-os/
-- Instalar para Windows https://redis.io/docs/getting-started/installation/install-redis-on-windows/
- Haber instalado Celery
-- pip install celery
- Haber instalado requests
-- pip install requests

# Instrucciones de ejecución

* Ubicarse en la carpeta  (Esto por cada terminal que abra debe ejecutar)

    ```
    cd experimento_arquitectura/
    source venv/Scripts/activate
- Para ver el listado de librerias
    ```
    pip list
- Sino funciona debe instalar 
    ```
    python3 -m pip install --upgrade pip
- Para instalar las librerias ejecutar - Instalar librerias requeridas (ver archivo requirement.txt)
    ```
    python3 -m pip install -r requirements.txt
- Ejecutar el componente api_gateway en el puerto 5000
    ```cd api_gateway/
    flask run -p 5000
- Ejecutar el componente plataforma_mensajeria en puerto 5001
    ```cd plataforma_mensajeria/
    flask run -p 5001
- Ejecutar el componente administrar_reglas en el puerto 5002 
    ```cd administrar_reglas/
    flask run -p 5002
- Ejecutar REDIS
    ```
    redis-server
- Iniciar Celery en el compomente plataforma_mensajeria 
    ```cd plataforma_mensajeria/
    celery -A tareas worker -l info
6. Crear un request en postman usando la interfaz del gateway:
    http://127.0.0.1:5000/crear_regla
    y el body:
    ```
    {
        "nombre":"regla 1",
        "descripcion":"regla_1"
    }
    O importar el proyecto en postman https://www.getpostman.com/collections/2a29ce6a6799a39012a2
