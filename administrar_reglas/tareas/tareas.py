from unicodedata import name
from app import db
from modelos import Regla, ReglaSchema
import os
from celery import Celery
from celery.signals import task_postrun

celery_app=Celery('task',broker='redis://localhost:6379/0')

regla_schema = ReglaSchema()

@celery_app.task(name='table.registrar')
def crear_regla(regla):
    nuevo= Regla(nombre=regla.json["nombre"], descripcion=regla.json["descripcion"])
    db.session.add(nuevo)
    db.session.commit()

@task_postrun.connect()
def close_session(*args,**kwargs):
    db.session.remove()