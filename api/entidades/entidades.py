class Concessionaria:
    # Criando o método construtor ao usar o __init__. O construtor é chamado quando cria-se um novo objeto na classe
    def __init__(self, nome, ano_fabricacao, cor, marca):
        # Criação de atributos privados onde inicia-se com o valor passado como nome
        self.__nome = nome
        self.__ano_fabricacao = ano_fabricacao
        self.__cor = cor
        self.__marca = marca

    # É um decorador usado para criar o método getter, permitindo acessar um atributo privado como se fosse público.
    @property
    # Quando chama-se o objeto.nome, ele retorna o valor.
    def nome(self):
        return self.__nome
    # É um decorador usado para modificar o valor do atributo privado como se fosse público.
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def ano_fabricacao(self):
        return self.__ano_fabricacao
    @ano_fabricacao.setter
    def ano_fabricacao(self, novo_ano):
        self.__ano_fabricacao = novo_ano

    @property
    def cor(self):
        return self.__cor
    @cor.setter
    def cor(self, nova_cor):
        self.__cor = nova_cor

    @property
    def marca(self):
        return self.__marca
    @marca.setter
    def marca(self, nova_marca):
        self.__marca = nova_marca