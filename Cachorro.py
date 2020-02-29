# BIBLIOTECA RANDOM QUE SERÁ USADA PARA GERAR O NÚMERO DE FILHOTES
from random import randint

class Cachorro():
    # INICIALIZADOR
    def __init__(self, nome, raca, sexo, idade):
        self.nome = nome
        self.raca = raca
        self.sexo = sexo
        self.idade = idade
        self.energia = 100
        self.num_filhotes = 0

    # METODO QUE OBTEM OS DADOS DOS 6 ATRIBUTOS
    def obter_dados(self):
        # RETORNA OS SEIS DADOS DO CACHORRO
        return "Nome: {} \nRaça: {} \nSexo: {} \nIdade : {} \nEnergia: {} \nNúmero de Filhos : {}\n".format(self.nome, self.raca, self.sexo, self.idade, self.energia, self.num_filhotes)

    # METODO QUE FAZ O CACHORRO COMER E AUMENTAR SUA ENERGIA
    def comer(self, comida):
        if self.energia <= 50:
            if comida == "R":
                #R É RAÇÃO
                self.energia += 50
            elif comida == "C":
                #C É CARNE
                self.energia += 40
            elif comida == "L":
                #L É LEGUME
                self.energia += 30
            print("Cão alimentado! Energia atual: {}".format(self.energia))
        else:
            print("O cachorro não precisa comer")

    # MÉTODO QUE FAZ O CACHORRO BRINCAR E DIMINUI SUA ENERGIA
    def brincar(self, brincadeira):
        if self.energia >= 40:
            if brincadeira == "B":
                #B É BUSCAR A BOLINHA
                self.energia -= 30
            elif brincadeira == "S":
                #S É SALTAR
                self.energia -= 20
            elif brincadeira == "G":
                #G É GIRAR PELO CHÃO
                self.energia -= 10
            print("O cão brincou! Energia atual: {}".format(self.energia))
        else:
            print("O cachorro está cansado")

    # MÉTODO QUE VERIFICA SE O CÃO PODE CRUZAR OU NÃO
    def pode_cruzar(self, parc):
        if self.idade >= 1 and self.idade <= 9 and parc.idade >= 1 and parc.idade <= 9 and self.raca == parc.raca and self.energia >= 80 and parc.energia >= 80 and self.sexo != parc.sexo:
            return True
        else:
            return False

    # MÉTODO QUE FAZ O CRUZAMENTO DOS CÃES
    def cruzar(self, parc):
        if self.pode_cruzar(parc):
            filhos = randint(3, 10)
            self.energia -= 50
            parc.energia -= 50
            self.num_filhotes += filhos
            parc.num_filhotes += filhos
            return filhos
        else:
            print("NÃO DEU PARA REALIZAR O CRUZAMENTO")







