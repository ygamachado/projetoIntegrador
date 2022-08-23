import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='ong'
)


class Animal ():
    def __init__(self, nome, idade, raca, sexo, porte_animal, deficiencia, vacina):
        self.nome = nome
        self.idade = idade
        self.raca = raca
        self.sexo = sexo
        self.porte_animal = porte_animal
        self.deficiencia = deficiencia
        self.vacinacao = vacina


    def cadastroanimal(self):
        # nome do animal se tiver uma colera e tiver o nome na coleira tbm
        conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='ong'
        )
        cursor=conexao.cursor()

        print(' CADASTRO DE ANIMAIS')
        print('')

        print('o animal pssui nome? s/n')
        vericada=input('digite:')

        if (vericada=='s') or (vericada=='S'):
            print('digte o nome do animal')
            nomeanimal=input('digite:')

        else:
            print('')
    # cor do animal
    print('digite a cor do animal')
    coranimal=("digte:")
    print('')
        # porte do animal
    print(' porte do animal\n piqueno porte digite: (P)\n medio porte digite: (M)\n auto porte digite (A)')
    veriporte=input('digite:')

    if (veriporte=='p') or (veriporte=='P'):
        porte='P'

    elif (veriporte=='m') or (veriporte=='M'):
        porte='M'

    elif (veriporte=='a') or (veriporte=='A'):
        porte='a'

    else:
        print('ERRO')
        print('NENHUMA DAS OPÇÕ~ES FIU SELECINADAS')
        print('volte ao menu com a tecla ()')












        cursor.close()
        conexao.close()




