import mysql.connector

class formulario:
    def __init__(self, moradores, motivo, possui_animais, animais, profissao, moradia, favor_adocao, despesas, rotina, tempo_fora):
        self.moradores = moradores
        self.motivo_adocao = motivo
        self.possui_animais = possui_animais
        self.quais_animais = animais
        self.profissao = profissao
        self.tipo_moradia = moradia
        self.favor_adocao = favor_adocao
        self.condicao_despesas = despesas
        self.rotina = rotina
        self.tempo_fora = tempo_fora

    @classmethod
    def formulario_perguntas(self, id_adotante, moradores, motivo, possui_animais, animais, profissao, moradia, favor_adocao, despesas, rotina, tempo_fora):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="ong"
        )
        cursor = connection.cursor()
        comando_insert = "INSERT INTO formulario (id_adotante, moradores, motivo_adocao, possui_animais, quais_animais, profissao, tipo_moradia, favor_adocao, condicao_despesas, rotina, tempo_fora) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        data = (
            f'{id_adotante}',
            f'{moradores}',
            f'{motivo}',
            f'{possui_animais}',
            f'{animais}',
            f'{profissao}',
            f'{moradia}',
            f'{favor_adocao}',
            f'{despesas}',
            f'{rotina}',
            f'{tempo_fora}'
        )
        cursor.execute(comando_insert, data)
        connection.commit()
        print("\n===================== Formulário enviado com sucesso! =====================")
        cursor.close()
        connection.close()

    def formularios_semresposta():
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="ong"
        )
        cursor = connection.cursor()
        select = f"SELECT id_formulario, id_adotante, moradores, motivo_adocao, possui_animais, quais_animais, profissao, tipo_moradia, favor_adocao, condicao_despesas, rotina, tempo_fora, adocao_aprovada FROM formulario WHERE adocao_aprovada IS NULL;"
        cursor.execute(select)
        results = cursor.fetchall()
        cursor.close()
        connection.close()
        for result in results:
            print("\n====================\nID do formulário:", result[0], "\n====================\n\nID do adotante:", result[1], "\n--------------------\nMoradores da Residência:", result[2], "\n--------------------\nMotivo da adoção:", result[3], "\n--------------------\nPossui animais:", result[4], "\n--------------------\nQuais animais possui:", result[5], "\n--------------------\nProfissão:", result[6], "\n--------------------\nTipo de Moradia:", result[7], "\n--------------------\nTodos os moradores estão à favor da adoção:", result[8], "\n--------------------\nPossui condição de arcar com as despesas:", result[9], "\n--------------------\nSua rotina:", result[10], "\n--------------------\nTempo que passa fora de casa:",  result[11], "\n--------------------\nAdoção aprovada:", result[12], "\n--------------------")
        if len(results) == 0:
            print("\n==================== Não há formulários pendentes ====================")

    def formularios_foramaprovados():
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="ong"
        )
        cursor = connection.cursor()
        select = f"SELECT id_formulario, id_adotante, moradores, motivo_adocao, possui_animais, quais_animais, profissao, tipo_moradia, favor_adocao, condicao_despesas, rotina, tempo_fora, adocao_aprovada FROM formulario WHERE adocao_aprovada = 's';"
        cursor.execute(select)
        results = cursor.fetchall()
        cursor.close()
        connection.close()
        for result in results:
            print("\n====================\nID do formulário:", result[0], "\n====================\n\nID do adotante:", result[1], "\n--------------------\nMoradores da Residência:", result[2], "\n--------------------\nMotivo da adoção:", result[3], "\n--------------------\nPossui animais:", result[4], "\n--------------------\nQuais animais possui:", result[5], "\n--------------------\nProfissão:", result[6], "\n--------------------\nTipo de Moradia:", result[7], "\n--------------------\nTodos os moradores estão à favor da adoção:", result[8], "\n--------------------\nPossui condição de arcar com as despesas:", result[9], "\n--------------------\nSua rotina:", result[10], "\n--------------------\nTempo que passa fora de casa:",  result[11], "\n--------------------\nAdoção aprovada:", result[12], "\n--------------------")
        if len(results) == 0:
            print("\n==================== Não há formulários aprovados ====================")

    def formularios_foramreprovados():
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="ong"
        )
        cursor = connection.cursor()
        select = f"SELECT id_formulario, id_adotante, moradores, motivo_adocao, possui_animais, quais_animais, profissao, tipo_moradia, favor_adocao, condicao_despesas, rotina, tempo_fora, adocao_aprovada FROM formulario WHERE adocao_aprovada = 'n';"
        cursor.execute(select)
        results = cursor.fetchall()
        cursor.close()
        connection.close()
        for result in results:
            print("\n====================\nID do formulário:", result[0], "\n====================\n\nID do adotante:", result[1], "\n--------------------\nMoradores da Residência:", result[2], "\n--------------------\nMotivo da adoção:", result[3], "\n--------------------\nPossui animais:", result[4], "\n--------------------\nQuais animais possui:", result[5], "\n--------------------\nProfissão:", result[6], "\n--------------------\nTipo de Moradia:", result[7], "\n--------------------\nTodos os moradores estão à favor da adoção:", result[8], "\n--------------------\nPossui condição de arcar com as despesas:", result[9], "\n--------------------\nSua rotina:", result[10], "\n--------------------\nTempo que passa fora de casa:",  result[11], "\n--------------------\nAdoção aprovada:", result[12], "\n--------------------")
        if len(results) == 0:
            print("\n==================== Não há formulários reprovados ====================")

    @classmethod
    def aprovar_formularios(self, aprovacao, id_formulario):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="ong"
        )
        cursor = connection.cursor()

        comando_update = f"UPDATE formulario SET id_formulario = %s, adocao_aprovada = %s WHERE id_formulario = '{id_formulario}'"
        data = (
            f'{id_formulario}',
            f'{aprovacao}'
        )
        cursor.execute(comando_update, data)
        connection.commit()

        cursor.close()
        connection.close()
