from flask import request
from ..modelos import db, Usuario, UsuarioSchema
from flask_restful import Resource
from flask_jwt_extended import  create_access_token
usuario_schema = UsuarioSchema()

class VistaAutenticacion(Resource):

    
    def post(self):
        usuario = Usuario.query.filter(Usuario.usuario == request.json["usuario"],
                                       Usuario.contrasena == request.json["contrasena"]).first()
        db.session.commit()
        if usuario is None:
            return "El usuario no existe", 404
        else:
            token_de_acceso = create_access_token(identity=usuario.id)
            return {"token": token_de_acceso}