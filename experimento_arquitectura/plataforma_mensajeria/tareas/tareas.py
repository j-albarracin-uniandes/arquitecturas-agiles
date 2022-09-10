import os
from celery import Celery
from celery.signals import task_postrun
import requests
from requests.exceptions import ConnectionError


celery_app = Celery('tasks', broker='redis://localhost:6379/0')

@celery_app.task(name='crear_regla')
def crear_regla(nombre_regla, descripcion_regla, retry):
    try:
        payload = dict(nombre=nombre_regla, descripcion=descripcion_regla)
        content = requests.post('http://127.0.0.1:5002/reglas', json=payload)
        print(content.json())
        print(payload)
        if content.status_code == 200:
            return {'mensaje':'Regla Creada Exitosamente'}, 200            
        else:
            retryOn(nombre_regla, descripcion_regla, retry)
            return content.json(), 500
    except:        
        print('****** 28 ******')
        retryOn(nombre_regla, descripcion_regla, retry)
   
    

def retryOn(nombre_regla, descripcion_regla, retry):
    retry += 1
    args = (nombre_regla, descripcion_regla, retry)
    timetorun = retry * 5
    if(timetorun > 50): timetorun = 60
    print('******** send retry: ' + str(retry) + ' on ' + str(timetorun))
    crear_regla.apply_async(args, countdown=timetorun)
