from administrar_usuarios import create_app
from .modelos import db, Usuario
from flask_restful import Api
from .vistas import VistaAutenticacion
from flask_jwt_extended import JWTManager
app = create_app('default')
app.config['JWT_SECRET_KEY'] = 'frase-secreta'
app_context = app.app_context()
app_context.push()

db.init_app(app)
#db.create_all()

api = Api(app)
api.add_resource(VistaAutenticacion, '/auth')

jwt = JWTManager(app)