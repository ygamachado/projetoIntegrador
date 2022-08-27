import Adotante
import Adotante_Endereço

# -- Método para cadastro de adotante

def cadastrando_adotante():
    print("\n================ Dados Pessoais ================")
    id_adotante = input("\nID do Adotante: ")
    usuario = input("\nNome de Usuário (Limite de 25 dígitos): ")
    senha = input("\nSenha (Limite de 8 dígitos): ")
    nome = input("\nNome Completo: ")
    nascimento = input("\nData de Nascimento AA-MM-DD: ")
    telefone1 = input("\nNúmero de Telefone: ")
    escolha = input("\nAdicionar número de telefone opcional? s/n ")
    if (escolha == "s") or (escolha == "S"):
        telefone2 = input("\nNúmero de Telefone Opcional: ")
    else:
        telefone2 = None
    email = input("\nE-mail: ")
    print("\n================ Dados de Endereço ================")
    id_endereco = input("\nID do Endereço: ")
    logradouro = input("\nLogradouro: ")
    numero = input("\nNúmero da Residência: ")
    bairro = input("\nBairro: ")
    cidade = input("\nCidade: ")
    uf = input("\nUF: ")
    cep = input("\nCEP: ")
    dados_end = Adotante_Endereço.endereco(id_endereco, logradouro, numero, bairro, cidade, uf, cep, id_adotante, nome, nascimento, telefone1, telefone2, email, usuario, senha)
    dados_ad = Adotante.adotante(id_adotante, nome, nascimento, telefone1, telefone2, email, usuario, senha)
    confirmar = input("\nConfirmar cadastro? s/n ")
    if (confirmar == "s") or (confirmar == "S"):
        dados_end.cadastro_endereco(id_endereco, id_adotante, logradouro, numero, bairro, cidade, uf, cep)
        dados_ad.cadastro_adotante(id_adotante, nome, nascimento, telefone1, telefone2, email, usuario, senha)
    else:
        print("\n===================== Os dados não foram salvos =====================")



def cadastroanimal():

    print(' CADASTRO DE ANIMAIS')
    print('')


    # n sei ara q serve esse id exame
    print('digite o exame valor a enserir terar de ser inteiro')
    idexame = int(input('digite:'))

    print('')


    # nome do animal se tiver
    print('o animal possui nome? s/n')
    verino = input('digite:')

    if (verino == 's') or (verino == 'S'):
        print('digite o nome que esta na coleira:')
        nomeanimal = input('digite:')

    elif (verino == 'n') or (verino == 'N'):
        nomeanimal='N'


    else:
        print('ERRO')
        print('NENHUMA DAS OPÇÕES FOI SELECINADAS')
        print('volte ao menu com a tecla ()')
    print('')


    # cor do animal
    print('digite a cor do animal')
    coranimal =input("digite:")
    print('')


    # porte do animal
    print(' porte do animal:\n piqueno porte digite: (P)\n medio porte digite: (M)\n auto porte digite (A)')
    veriporte = input('digite:')

    if (veriporte == 'p') or (veriporte == 'P'):

        porte = 'P'

    elif (veriporte == 'm') or (veriporte == 'M'):

        porte = 'M'

    elif (veriporte == 'a') or (veriporte == 'A'):

        porte = 'A'


    else:
        print('ERRO')
        print('NENHUMA DAS OPÇÕES FOI SELECINADAS')
        print('volte ao menu com a tecla ()')

    print('')

    # RAÇA DO ANIMAL
    print('digite a raça/especie do animal')
    raca = input('digite:')
    print('')


    # idade estimada do animal
    print('idade estimada do animal')
    idade =input('digite:')
    print('')


    # DISPONIVEL PARA DOAÇAO

    print('disponivel para a doeção? S/N')
    veridis=input('digite:')

    if (veridis == 's') or (veridis == 'S'):
        disponivel = 'S'


    elif (veridis == 'n') or (veridis == 'N'):

        disponivel = 'N'


    else:
        print('ERRO')
        print('COMANDO NÃO FOI SEGUIDO CORRETAMENTE')
    print('')



# adotado?
    print('o animal ja foi adotado? S/N')
    adotado = input('digite:')
    print('')


    # deficincia

    print('o animal possui alguma deficiencia fisica? s/n')
    veridef = input('digite:')

    if (veridef == 's') or (veridef == 'S'):

        deficiencia ='S'

    elif (veridef == 'n') or (veridef == 'N'):
        deficiencia = 'N'

    else:
        print('ERRO')

        print('COMANDO NÃO FOI SEGUIDO CORRETAMENTE')
    print('')


    # animal castardo
    print('animal é castrado? S/N')
    castrado =input ('digite:')
    print('')


    #  exameas animal
    print('o animal a fez algum exame? S/N')
    veriex = input('digite:')

    if (veriex == 's') or (veriex == 'S'):
        print('quantos?')
        enxames = int(input(('digite:')))

    elif (veriex == 'n') or (veriex == 'N'):
        enxames = 0

    else:
        print('ERRO')
        print('COMANDO NÃO FOI SEGUIDO CORRETAMENTE')
    print('')


    # local que o animal foi encotrado
    print('qual foi o local que o animal foi encontrado/resgatado')
    localecontrado = input('digite:')
    print('')


    # data que o animal foi encontrado

    print('data que o animal foi encotrado')
    dataresgate = input('digite:')
    print('')

    print('CADASTRO C0NCLUIDO COM SUCESSO !!')