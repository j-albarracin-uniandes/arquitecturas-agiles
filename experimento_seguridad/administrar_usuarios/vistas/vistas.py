from flask import request
from ..modelos import db, Usuario, UsuarioSchema
from flask_restful import Resource

regla_schema = UsuarioSchema()

class VistaUsuario(Resource):

    
    def post(self):
        usuario = Usuario.query.get_or_404(request.json['id'])
        usuario.nombre=request.json['nombre']
        usuario.apellido=request.json['apellido']
        usuario.correo_electronico=request.json['correo_electronico']
        db.session.commit()
        return {"mensaje": "Usuario editado exitosamente"}