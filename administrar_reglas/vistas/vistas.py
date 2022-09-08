""" import requests
from modelos import db, Regla
from flask_restful import Resource
class VistaRegla(Resource):
    def post(self,request):
        nuevo= Regla(nombre=request.json["nombre"], descripcion=request.json["descripcion"])
        db.session.add(nuevo)
        db.session.commit()
        return {"mensaje": "Regla creada exitosamente", "id": nuevo.id} """