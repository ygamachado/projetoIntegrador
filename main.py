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
