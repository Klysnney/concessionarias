from api import db

class Concessionaria(db.Model):
    __tablename__ = "concessionaria"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nome = db.Column(db.String(20), nullable=False)
    ano_fabricacao  = db.Column(db.Integer, nullable=False)
    cor = db.Column(db.String(20), nullable= False)
    marca = db.Column(db.String(20), nullable= False)
