# Instrucciones de ejecucion

1. Instalar librerias requeridas (ver archivo requirement.txt)
2. Ejecutar el componente api_gateway en el puerto 5000 (flask run -p 5000)
3. Ejecutar el componente plataforma_mensajeria en puerto 5001 (flask run -p 5001)
4. Ejecutar el componente administrar_regla en el puerto 5002 (flask run -p 5002)
5. Iniciar Celery en el compomente plataforma_mensajeria (celery -A tareas worker -l info)
6. Crear un request en postman usando la interfaz del gateway:
http://127.0.0.1:5000/crear_regla

y el body:
```
{
    "nombre":"regla 1",
    "descripcion":"regla_1"
}
```
