import mysql.connector

class adotante:
    def __init__(self, id_adotante, nome, nascimento, telefone1, telefone2, email, usuario, senha):
        self.id_adotante = id_adotante
        self.nome = nome
        self.data_nasc = nascimento
        self.telefone1 = telefone1
        self.telefone2 = telefone2
        self.email = email
        self.usuario = usuario
        self.senha = senha

    @classmethod
    def cadastro_adotante(self, id_adotante, nome, nascimento, telefone1, telefone2, email, usuario, senha):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="ong"
        )
        cursor = connection.cursor()
        comando_insert = "INSERT INTO adotante (id_adotante, nome, data_nasc, telefone1, telefone2, email, usuario, senha) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        data = (
            f'{id_adotante}',
            f'{nome}',
            f'{nascimento}',
            f'{telefone1}',
            f'{telefone2}',
            f'{email}',
            f'{usuario}',
            f'{senha}'
        )
        cursor.execute(comando_insert, data)
        connection.commit()
        print("\n===================== Cadastro concluído com sucesso =====================")
        cursor.close()
        connection.close()