from plataforma_mensajeria import create_app
from flask_restful import Resource, Api
import requests

app = create_app('default')
app_contex = app.app_context()
app_contex.push()

# class VistaAdministrarRegla(Resource):
#     def get(self):
#         return 'mensaje creado'

# api = Api(app)
# api.add_resource(VistaAdministrarRegla, '/crear_regla')