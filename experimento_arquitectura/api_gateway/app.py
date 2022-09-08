
from api_gateway import create_app
from flask_restful import Resource, Api
from flask import Flask, request
import requests
import json
from celery import Celery

celery_app = Celery(__name__, broker='redis://localhost:6379/0')

app = create_app('default')
app_contex = app.app_context()
app_contex.push()

api = Api(app)

@celery_app.task(name='crear_regla')
def crear_regla(nombre_regla, descripcion_regla):
    pass

class VistaAdministrarReglas(Resource):

    def post(self):
        nombre_regla = request.json['nombre']
        descripcion_regla = request.json['descripcion']
        args = (nombre_regla, descripcion_regla)
        crear_regla.apply_async(args)
        return {'mensaje':'Creacion de regla recibida'}, 200

api.add_resource(VistaAdministrarReglas, '/crear_regla')