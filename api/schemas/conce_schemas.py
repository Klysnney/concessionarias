from api import ma
from..models import conce_models
from marshmallow import fields

class ConcessionariaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = conce_models.Concessionaria
        load_instance = True
        fields = ('id', 'nome', 'ano_fabricacao', 'cor', 'marca')

    nome = fields.String(required=True)
    ano_fabricacao = fields.Integer(required=True)
    cor = fields.String(required=True)
    marca = fields.String(required=True)