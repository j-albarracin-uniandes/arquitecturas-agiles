import os
from celery import Celery
from celery.signals import task_postrun
import requests

celery_app = Celery('tasks', broker='redis://localhost:6379/0')

@celery_app.task(name='crear_regla')
def crear_regla(nombre_regla, descripcion_regla):
    payload = dict(nombre=nombre_regla, descripcion=descripcion_regla)
    content = requests.post('http://127.0.0.1:5002/reglas', json=payload)
    print(content.json())
    print(payload)
    if content.status_code == 200:
        return {'mensaje':'Regla Creada Exitosamente'}, 200            
    else:
        return content.json(), 500