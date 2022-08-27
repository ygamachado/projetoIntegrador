import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='ong'
)


class Animal ():


    def __init__(self,idexame, nomeanimal, cor, idade, raca, sexo, porte,disponivel, deficiencia, adotado,castrado,exames,localecontrado,dataresgate):
        self.nome = nomeanimal
        self.idade = idade
        self.raca = raca
        self.sexo = sexo
        self.porte_animal = porte
        self.deficiencia = deficiencia
        self.ideexame=idexame
        self.coranimal=cor
        self.disponivel_doacao=disponivel
        self.adotado=adotado
        self.castrado=castrado
        self.exames=exames
        self.localencontrado=localecontrado
        self.dataresgate=dataresgate

    @classmethod
    def cadastrar(self,idexame, nomeanimal, coranimal, idade, raca, porte,disponivel, deficiencia, adotado,castrado,exames,localecontrado,dataresgate):
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='ong'
        )
        cursor = connection.cursor()
        comando = f'insert into cad_animal(id_exame, nome, cor, porte, raça, idade, disponivel, adotado, deficiente, castrado, quant_exames,local_encontro, data_encontro) values("{idexame}","{nomeanimal}","{coranimal}","{porte}","{raca}","{idade}","{disponivel}","{adotado}","{deficiencia}","{castrado}","{exames}","{localecontrado}","{dataresgate}")'
        data=(

            f"{idexame}",
            f"{nomeanimal}",
            f"{coranimal}",
            f"{porte}",
            f"{raca}",
            f"{idade}",
            f"{disponivel}",
            f"{adotado}",
            f"{deficiencia}",
            f"{castrado}",
            f"{exames}",
            f"{localecontrado}",
            f"{dataresgate}"
        )
        cursor.execute(comando,data)
        connection.commit()
        print("\n===================== Cadastro concluído com sucesso =====================")
        cursor.close()
        connection.close()












