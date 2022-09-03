import mysql.connector

class adotante:
    def __init__(self, id_adotante, nome, nascimento, telefone1, telefone2, email, usuario, senha):
        self.__id_adotante = id_adotante
        self.__nome = nome
        self.__data_nasc = nascimento
        self.__telefone1 = telefone1
        self.__telefone2 = telefone2
        self.__email = email
        self.__usuario = usuario
        self.__senha = senha

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

        def consultar_adotantes():
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="ong"
            )
            cursor = connection.cursor()

            comando_select = f"SELECT * FROM adotante"

            cursor.execute(comando_select)
            results = cursor.fetchall()

            cursor.close()
            connection.close()

            for result in results:
                print(result)