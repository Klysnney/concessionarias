from api import api
from flask_restful import Resource
from..schemas import conce_schemas
from flask import request, make_response, jsonify
from..services import conce_services
from api.entidades.entidades import Concessionaria

class ConcessionariaViews(Resource):
    def post(self):
        # Validação dos dados no Schema
        carro = conce_schemas.ConcessionariaSchema()
        validate = carro.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json['nome']
            ano_fabricacao = request.json['ano_fabricacao']
            cor = request.json['cor']
            marca = request.json['marca']

        # Método Construtor
        novo_carro = Concessionaria(nome=nome,
                                    ano_fabricacao=ano_fabricacao,
                                    cor=cor,
                                    marca=marca)
        # Cadastrando em conce_services.py
        resultado = conce_services.cadastro_carros(novo_carro)
        x = carro.jsonify(resultado)
        return make_response(x, 201)
    def get(self):
        carro = conce_services.listar_carros()
        carro_schema = conce_schemas.ConcessionariaSchema(many=True)
        return make_response(carro_schema.jsonify(carro), 200)

class ConcessionariaViewsID(Resource):
    def get(self,id):
        carro = conce_services.listagem_carros_id(id)
        if carro is None:
            return make_response(jsonify("Carro não encontrado"), 404)
        carro_schema = conce_schemas.ConcessionariaSchema()
        return make_response(carro_schema.jsonify(carro), 200)

    def put(self, id):
        carro = conce_services.listagem_carros_id(id)
        if carro is None:
            return make_response(jsonify("Carro não encontrado"), 404)
        carro_schema = conce_schemas.ConcessionariaSchema()
        validate = carro_schema.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json['nome']
            ano_fabricacao = request.json['ano_fabricacao']
            cor = request.json['cor']
            marca = request.json['marca']

        novo_carro = Concessionaria(nome=nome,
                                    ano_fabricacao=ano_fabricacao,
                                    cor=cor,
                                    marca=marca)
        conce_services.atualizar_mercadoria(carro, novo_carro)
        carro_atualizado = conce_services.listagem_carros_id(id)
        return make_response(carro_schema.jsonify(carro_atualizado), 200)

    def delete(self, id):
        carro_registrado = conce_services.listagem_carros_id(id)
        if carro_registrado is None:
            return make_response(jsonify("Carro não encontrado"), 404)
        else:
            conce_services.deletar_carro(carro_registrado)
            return make_response(jsonify("Carro excluído com sucesso"), 204)


api.add_resource(ConcessionariaViews, '/concessionaria')
api.add_resource(ConcessionariaViewsID, '/concessionaria/<int:id>')

