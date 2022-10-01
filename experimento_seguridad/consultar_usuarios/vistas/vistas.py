from flask import request
from ..modelos import db, Usuario, UsuarioSchema
from flask_restful import Resource
from flask_jwt_extended import jwt_required

usuario_schema = UsuarioSchema()

class VistaUsuario(Resource):

    @jwt_required()
    def post(self):
        return usuario_schema.dump(Usuario.query.get_or_404(request.json['id']))