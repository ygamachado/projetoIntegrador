class Animal():
    def __init__(self, nome,idade, raca, sexo, porte_animal, deficiencia,vacina):
        self.nome=nome
        self.idade=idade
        self.raca=raca
        self.sexo=sexo
        self.porte_animal=porte_animal
        self.deficiencia=deficiencia
        self.vacinacao=vacina
d
        def __init__(self,nome):
            self.nome=nome

            veri_coleira=input('se o animal possui coleira digite (S), senao (N)')

            if(veri_coleira =='s'or veri_coleira=='S'):
                print('digite o nome do animal')
                nome=input('')


            else:
                print('continue o cadastro')

    def vacin_animais (self):

        print('digite (S) se  animal é vacinado\n digite(N) se o animal não for vacinado\n ')
        print('digite(NS) se não ha informações se o animal é vacinado ')
        veri_vacina=input('')

        if (veri_vacina=='s'or veri_vacina=='S'):
            print('quantas vacinas oanimal tomo')
            tipos_vacina=[]
            quantidade_vacina=int(input(''))

            print('quais foram as vacinas que o animal tomou')
            tipos_vacina.append(input(''))


























# funçoes: se possui deficiencia, animal castrado