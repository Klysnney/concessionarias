from..models import conce_models
from api import db

def cadastro_carros(carro):
    carro_cadastrar = conce_models.Concessionaria(nome=carro.nome,
                                                  ano_fabricacao=carro.ano_fabricacao,
                                                  cor=carro.cor,
                                                  marca=carro.marca)
    db.session.add(carro_cadastrar)
    db.session.commit()
    return carro_cadastrar
def listar_carros():
    carros = conce_models.Concessionaria.query.all()
    return carros

def atualizar_mercadoria(carro_antigo, carro_novo):
    carro_antigo.nome = carro_novo.nome
    carro_antigo.ano_fabricacao = carro_novo.ano_fabricacao
    carro_antigo.cor = carro_novo.cor
    carro_antigo.marca = carro_novo.marca
    db.session.commit()

def listagem_carros_id(id):
    carro = conce_models.Concessionaria.query.filter_by(id=id).first()
    return carro

def deletar_carro(id):
    db.session.delete(id)
    db.session.commit()