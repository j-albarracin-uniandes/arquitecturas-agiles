
from api_gateway import create_app
from flask_restful import Resource, Api
from flask import Flask, request
import requests
import json

app = create_app('default')
app_contex = app.app_context()
app_contex.push()

api = Api(app)

class VistaAdministrarUsuarios(Resource):

    def post(self):
      
        content = requests.post('http://127.0.0.1:5000/usuario', json=request.json)
        print(content.json())      
        if content.status_code == 200:
            return content.json(), 200            
        else:           
            return content.json(), 500

api.add_resource(VistaAdministrarUsuarios, '/editar_usuario')