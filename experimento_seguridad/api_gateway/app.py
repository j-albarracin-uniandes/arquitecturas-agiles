
from api_gateway import create_app
from flask_restful import Resource, Api
from flask import Flask, request
import requests
import json
from flask_jwt_extended import jwt_required,JWTManager
app = create_app('default')
app.config['JWT_SECRET_KEY'] = 'frase-secreta'
app_contex = app.app_context()
app_contex.push()

api = Api(app)

class VistaAdministrarUsuarios(Resource):
    @jwt_required()
    def post(self):
      
        content = requests.post('http://127.0.0.1:5001/usuario', json=request.json)
           
        if content.status_code == 200:
            return content.json(), 200            
        else:           
            return content.json(), 500

class ConsultarUsuarios(Resource):    
    @jwt_required()
    def post(self):
      
        content = requests.post('http://127.0.0.1:5002/usuario-by-id', json=request.json, headers=request.headers)
          
        if content.status_code == 200:
            return content.json(), 200            
        else:           
            return content.json(), 500

class AutenticarUsuarios(Resource):    
    def post(self):
      
        content = requests.post('http://127.0.0.1:5003/auth', json=request.json)
          
        if content.status_code == 200:
            return content.json(), 200            
        else:           
            return content.json(), 500

api.add_resource(VistaAdministrarUsuarios, '/editar_usuario')
api.add_resource(ConsultarUsuarios, '/usuario-by-id')
api.add_resource(AutenticarUsuarios, '/auth')

jwt = JWTManager(app)