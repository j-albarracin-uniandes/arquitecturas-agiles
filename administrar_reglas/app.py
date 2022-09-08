from flask_restful import Api
from flask import Flask

from modelos import db
""" 
from vistas import VistaRegla """
app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reglas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app_context= app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

api =Api(app)


""" 
api.add_resource(VistaRegla,'/regla') """