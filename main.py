import Adotante
import Adotante_Endereço
import animal

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

def consultando_adotantes():
    print("\n================ Dados Pessoais dos Adotantes ================\n")
    selecionar_adotantes = Adotante.adotante.consultar_adotantes()
    print("\n================ Dados de Endereço dos Adotantes ================\n")
    selecionar_enderecos = Adotante_Endereço.endereco.consultar_enderecos()

def alterar_adotantes_pessoais():
    dados_adotantes()
    id_adotante = int(input("\nDigite o índice do adotante: "))
    alterar = Adotante.adotante.selecionar_adotantes(id_adotante)
    print("\nUsuário de ID", id_adotante, "selecionado")
    nome = input("\nNovo nome: ")
    nascimento = input("\nNova data de nascimento: ")
    telefone1 = input("\nNovo telefone: ")
    escolha = input("\nDeseja alterar/adicionar número de telefone opcional? s/n ")
    if (escolha == "s") or (escolha == "S"):
        telefone2 = input("\nNúmero de telefone opcional: ")
    else:
        telefone2 = None
    email = input("\nNovo e-mail: ")
    usuario = input("\nNovo nome de usuário: ")
    senha = input("\nNova senha: ")
    confirmar_dad = input("\nConfirmar alterações? s/n ")
    if (confirmar_dad == "s") or (confirmar_dad == "S"):
        alterar.atualizar_adotantes(id_adotante, nome, nascimento, telefone1, telefone2, email, usuario, senha)
    else:
        print("\n===================== Os dados não foram alterados =====================\n")

def alterar_adotantes_enderecos():
    dados_adotantes()
    id_endereco = int(input("\nDigite o índice de endereço do adotante: "))
    alterar_endereco = Adotante_Endereço.endereco
    print("\nUsuário do ID de endereço", id_endereco, "selecionado")
    logradouro = input("\nNovo logradouro: ")
    numero = input("\nNovo número de residência: ")
    bairro = input("\nNovo bairro: ")
    cidade = input("\nNova cidade: ")
    uf = input("\nNovo UF: ")
    cep = input("\nNovo CEP: ")
    confirmar_end = input("\nConfirmar alterações? s/n ")
    if (confirmar_end == "s") or (confirmar_end == "S"):
        alterar_endereco.atualizar_enderecos(id_endereco, id_endereco, logradouro, numero, bairro, cidade, uf, cep)
    else:
        print("\n===================== Os dados não foram alterados =====================")

def cadastroanimal():

    print(' CADASTRO DE ANIMAIS')
    print('')


    # n sei ara q serve esse id exame
    print('digite o exame valor a enserir terar de ser inteiro')
    id_exame = int(input('digite:'))

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
    cor =input("digite:")
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

        deficiente ='S'

    elif (veridef == 'n') or (veridef == 'N'):
        deficiente = 'N'

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
        exames = int(input(('digite:')))

    elif (veriex == 'n') or (veriex == 'N'):
        exames = 0

    else:
        print('ERRO')
        print('COMANDO NÃO FOI SEGUIDO CORRETAMENTE')
    print('')


    # local que o animal foi encotrado
    print('qual foi o local que o animal foi encontrado/resgatado')
    local_encontro = input('digite:')
    print('')


    # data que o animal foi encontrado

    print('data que o animal foi encotrado')
    data_encontro =input('digite:')
    print('')
    infor_animal = animal.Animal(id_exame, nomeanimal, cor, porte, raca,idade, disponivel, adotado, deficiente,castrado, exames, local_encontro, data_encontro)

    print('deseja salva? S/N')
    veriseiv=input('digite:')
    if(veriseiv=='s') or (veriseiv=='S'):

        infor_animal.cadastrar(id_exame,nomeanimal,cor,porte,raca,idade,disponivel,adotado,deficiente,castrado,exames,local_encontro,data_encontro)
        print('CADASTRO C0NCLUIDO COM SUCESSO !!')

    else:
        print("\n===================== Os dados não foram salvos =====================")


cadastroanimal()