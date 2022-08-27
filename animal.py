import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='ong'
)


class Animal ():


    def __init__(self,id_exame, nomeanimal, cor, idade, raca,porte,disponivel, deficiente, adotado,castrado,exames,local_encontro,data_encontro):

        self.ide_exame = id_exame
        self.nome = nomeanimal
        self.idade = idade
        self.raca = raca
        self.porte_animal = porte
        self.deficiente = deficiente
        self.cor=cor
        self.disponivel=disponivel
        self.adotado=adotado
        self.castrado=castrado
        self.exames=exames
        self.local_encontro=local_encontro
        self.data_encontro=data_encontro

    @classmethod
    def cadastrar(self,id_exame, nomeanimal, cor, idade, raca, porte,disponivel, deficiente, adotado,castrado,exames,local_encontro,data_encontro):
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='ong'
        )
        cursor = connection.cursor()
        comando = f'insert into cad_animal(id_exame, nome, cor, porte, raça, idade, disponivel, adotado, deficiente, castrado, quant_exames,local_encontro, data_encontro) values("{id_exame}","{nomeanimal}","{cor}","{idade}","{raca}","{disponivel}","{adotado}","{deficiente}","{castrado}","{exames}","{local_encontro}","{data_encontro}")'
        data=(

            f"{id_exame}",
            f"{nomeanimal}",
            f"{cor}",
            f"{porte}",
            f"{raca}",
            f"{idade}",
            f"{disponivel}",
            f"{adotado}",
            f"{deficiente}",
            f"{castrado}",
            f"{exames}",
            f"{local_encontro}",
            f"{data_encontro}"
        )
        cursor.execute(comando,data)
        connection.commit()
        print("\n===================== Cadastro concluído com sucesso =====================")
        cursor.close()
        connection.close()












