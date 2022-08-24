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

# INDICE DA FUNLAO DE CADASTRO DE ANIMAIS

    def cadastroanimal(self):



    # nome do animal se tiver uma colera e tiver o nome na coleira tbm
        conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='ong'

        )
        cursor = conexao.cursor()

        print(' CADASTRO DE ANIMAIS')
        print('')

        print('o animal pssui nome? s/n')
        vericada = input('digite:')

        if (vericada == 's') or (vericada == 'S'):
            print('digte o nome do animal')
            nomeanimal = input('digite:')

        else:
            print('')


# cor do animal
        print('digite a cor do animal')
        coranimal = ("digte:")
        print('')
# porte do animal
        print(' porte do animal\n piqueno porte digite: (P)\n medio porte digite: (M)\n auto porte digite (A)')
        veriporte = input('digite:')

        if (veriporte == 'p') or (veriporte == 'P'):

            porte = 'P'

        elif (veriporte == 'm') or (veriporte == 'M'):

            porte = 'M'

        elif (veriporte == 'a') or (veriporte == 'A'):

            porte = 'a'


        else:
            print('ERRO')
            print('NENHUMA DAS OPÇÕES FIU SELECINADAS')
            print('volte ao menu com a tecla ()')

# RAÇA DO ANIMAL
        print('digite a raça/especie do animal')
        raca = input('digite:')

# idade estimada do animal
        print('idade estimada do animal')
        idade = ('digite:')

# DISPONIVEL PARA DOAÇAO

        print('disponivel para a doeção? S/N')
        veridis = ('digite:')

        if (veridis == 's') or (veridis == 'S'):
            disponivel = 'DISPONIVEL'


        elif (veridis == 'n') or (veridis == 'N'):

            disponivel = 'INDISPOIVEL'


        else:
            print('ERRO')
            print('COMANDO NÃO FOI SEGUIDO CORRETAMENTE')
# deficincia

        print('o animal pessui possui alguma deficciencia fisica? s/n')
        veridef=input('digite:')

        if (veridef=='s') or (veridis=='S'):
                print('digtie a deficencia fisica do animal')
                deficiencia=input(('digite:'))

        elif (veridef=='n') or (veridis=='N'):
            deficiencia='sem dificiencia'

        else:
            print('ERRO')

            print('COMANDO NÃO FOI SEGUIDO CORRETAMENTE')

# animal castardo
        print('animal é castrado? S/N')
        castrado=('digite:')

#  exames animal
        print('o animal a fez algum exame? S/N')
        veriex=input('digite')

        if (veriex=='s') or (veriex=='S'):
            print('quantos?')
            enxames=input(('digite:'))

        elif (veriex=='n') or (veriex=='N'):
            enxames= 'sem exames'

        else:
            print('ERRO')
            print('COMANDO NÃO FOI SEGUIDO CORRETAMENTE')

# local que o animal foi encotrado
        print('qual foi o local que o animal foi encontrado/resgatado')
        localecontrado=input('digite:')

# data que o animal foi encontrado

        print('data que o animal foi encotrado')
        dataresgate=input('digite:')

        comando=f'insert into cad_animal(id_exame, nome, cor, porte, raça, idade, disponivel, adotado, deficiente, castrado, quant_exames,local_encontro, data_encontro) values('1 ', 'chulapa', 'preto', 'p', 'pinsher', '2', 'n', 'n', 'n', 's', '0', 'Rua Castroalves', 20220218);'







    # teno que dar 9 espaço para dicar no espaçamento serto
# espaçamento esta errado




        cursor.close()
        conexao.close()

    cadastroanimal()




