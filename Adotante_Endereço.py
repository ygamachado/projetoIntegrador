import mysql.connector
import Adotante

class endereco(Adotante.adotante):
    def __init__(self, id_endereco, logradouro, numero, bairro, cidade, uf, cep, id_adotante, nome, nascimento, telefone1, telefone2, email, usuario, senha):
        super().__init__(id_adotante, nome, nascimento, telefone1, telefone2, email, usuario, senha)
        self.id_endereco = id_endereco
        self.id_adotante = id_adotante
        self.logradouro = logradouro
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.uf = uf
        self.cep = cep

    @classmethod
    def cadastro_endereco(self, id_endereco, id_adotante, logradouro, numero, bairro, cidade, uf, cep):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="ong"
        )
        cursor = connection.cursor()
        comando_insert = "INSERT INTO endereço (id_endereço, id_adotante, logradouro, numero, bairro, cidade, uf, cep) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        data = (
            f'{id_endereco}',
            f'{id_adotante}',
            f'{logradouro}',
            f'{numero}',
            f'{bairro}',
            f'{cidade}',
            f'{uf}',
            f'{cep}'
        )
        cursor.execute(comando_insert, data)
        connection.commit()
        cursor.close()
        connection.close()
