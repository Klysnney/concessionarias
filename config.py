DEBUG = True

# Inserindo o banco de dados
USERNAME = "root"
PASSWORD = "Everton12"
SERVER = "localhost"
DB = "concessionaria"

# Usando o SQLALCHEMY para interagir com o banco de dados
SQLALCHEMY_DATABASE_URI = f'mysql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'
SQLALCHEMY_TRACK_MODIFICATIONS = True