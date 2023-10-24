# API de Concessionárias

Este é um projeto de API para gerenciar informações sobre concessionárias de veículos. Ele fornece recursos para cadastrar, listar, atualizar e excluir carros.

## Requisitos

- Python 3.7 ou superior
- Flask
- Flask-RESTful
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-Marshmallow
- MySQL

## Configuração

1. Clone o repositório:

   ```bash
   git clone https://github.com/Klysnney/concessionarias

## Uso

A API oferece endpoints para realizar operações CRUD (Criar, Ler, Atualizar, Excluir) em carros de concessionárias. Você pode interagir com a API usando ferramentas como o Postman ou o cURL.

## Endpoints

- **POST /concessionaria:** Cria um novo registro de carro.
- **GET /concessionaria:** Lista todos os carros.
- **GET /concessionaria/<int:id>:** Obtém os detalhes de um carro específico com base no ID.
- **PUT /concessionaria/<int:id>:** Atualiza os detalhes de um carro existente com base no ID.
- **DELETE /concessionaria/<int:id>:** Exclui um carro específico com base no ID.

- ## Exemplos

#### Criar, listar, atualizar e excluir carro
```http
POST /concessionaria
{
  "nome": "Carro Novo",
  "ano_fabricacao": 2023,
  "cor": "Vermelho",
  "marca": "Marca Nova"
}

GET /concessionaria

PUT /concessionaria/1
{
  "nome": "Carro Atualizado",
  "ano_fabricacao": 2022,
  "cor": "Azul",
  "marca": "Nova Marca"
}

DELETE /concessionaria/1



