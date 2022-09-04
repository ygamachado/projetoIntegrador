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
    def cadastrar(self,id_exame, nomeanimal, cor, porte,raca, idade,disponivel, adotado, deficiente,castrado,exames,local_encontro,data_encontro):
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='ong'
        )
        cursor = connection.cursor()
        comando = f'insert into cad_animal(id_exame, nome, cor, porte, raça, idade, disponivel, adotado, deficiente, castrado, quant_exames,local_encontro, data_encontro) values(%s,%s,%s,%s,%s,%s,%s,%s, %s,%s,%s,%s,%s)'
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

    @classmethod
    def atualizardadosanimais(self,id_animal,id_exame, nomeanimal, cor, porte,raca, idade,disponivel, adotado, deficiente,castrado,exames,local_encontro,data_encontro):

        connection=mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='ong'
        )

        cursor=connection.cursor()
        comando=f"UPDATE cad_animal SET id_animal=%s, id_exame=%s, nomeanimal=%s, cor=%s, porte=%s,raça=%s, idade=%s,disponivel=%s, adotado=%s, deficiente=%s,castrado=%s,exames=%s,local_encontro=%s,data_encontro=%s where id_animal='{id_animal}';"
        data=(
            f"{id_animal}",
            f"{id_exame}"
            f"{nomeanimal}",
            f"{cor}",
            f"{porte}",
            f"{raca}",
            f"{idade}",
            f"{disponivel}",
            f"{adotado}",
            f"{deficiente}" 
            f"{castrado}",
            f"{exames}",
            f"{local_encontro}",
            f"{data_encontro}"
        )
        cursor.execute(comando, data)
        connection.commit()
        cursor.close()
        connection.close()







