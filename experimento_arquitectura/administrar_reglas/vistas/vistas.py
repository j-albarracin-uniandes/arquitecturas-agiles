from flask import request
from ..modelos import db, Regla, ReglaSchema
from flask_restful import Resource

regla_schema = ReglaSchema()

class VistaReglas(Resource):

    def get(self):
        return [regla_schema.dump(regla) for regla in Regla.query.all()]
    
    def post(self):
        nueva_regla = Regla(nombre=request.json['nombre'],\
                            descripcion=request.json['descripcion'])
        db.session.add(nueva_regla)
        db.session.commit()
        return regla_schema.dump(nueva_regla)