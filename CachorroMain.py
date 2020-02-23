# POSSIBILITA O PROGRAMA SER ENCERRADO PELO EXIT(0)
from sys import exit
# IMPORT DA CLASSE CACHORRO
from Cachorro import Cachorro

def manipular_cachorro(cao_atual, lista_caes):
    lista_cruzamento = []
    try:
        opcao = 0
        while opcao != 5:
            opcao = int(input("OPÇÕES \n1) Ver dados do cão \n2) Alimentar \n3) Brincar \n4) Cruzar \n5) Menu Inicial \n"))
            lista_cruzamento.clear()
            if opcao == 1:
                print(lista_caes[cao_atual].obter_dados())
            elif opcao == 2:
                if lista_caes[cao_atual].energia <= 50:
                    alimentos = int(input("ALIMENTOS: \n1) RAÇÃO \n2) CARNE \n3) LEGUMES \n"))
                    if alimentos == 1:
                        lista_caes[cao_atual].comer("R")
                    elif alimentos == 2:
                        lista_caes[cao_atual].comer("C")
                    elif alimentos == 3:
                        lista_caes[cao_atual].comer("L")
                    else:
                        print("Opção Inválida")
                else:
                    print("O cachorro não precisa comer")
            elif opcao == 3:
                if lista_caes[cao_atual].energia >= 40:
                    brincadeira = int(input("BRINCADEIRAS: \n1) BUSCAR BOLINHA \n2) SALTAR \n3) GIRAR \n"))
                    if brincadeira == 1:
                        lista_caes[cao_atual].brincar("B")
                    elif brincadeira == 2:
                        lista_caes[cao_atual].brincar("S")
                    elif brincadeira == 3:
                        lista_caes[cao_atual].brincar("G")
                    else:
                        print("Opção Inválida")
                else:
                    print("O cachorro está cansado")
            elif opcao == 4:
                #for i in range(0, len(lista_caes)):
                    #if lista_caes[i].idade >= 1 and lista_caes[i].idade <= 9 and lista_caes[i].raca == lista_caes[cao_atual].raca and lista_caes[i].energia >= 80 and lista_caes[i].sexo != lista_caes[cao_atual].sexo:
                        #lista_cruzamento.append(lista_caes[i])
                #if len(lista_cruzamento) > 0:
                    #for i in range(0, len(lista_cruzamento)):
                        #print("CÃO Nº {}: {}\n".format(i, lista_caes[i].nome))
                for i in range(0, len(lista_caes)):
                    if lista_caes[cao_atual].pode_cruzar(lista_caes[i]):
                        lista_cruzamento.append(lista_caes[i])
                for i in range(0, len(lista_cruzamento)):
                    print("Cães disponíveis: \n{} - {} - {}% de energia - {} filhotes".format(i, lista_cruzamento[i].nome, lista_cruzamento[i].energia, lista_cruzamento[i].num_filhotes))
                if len(lista_cruzamento) > 0:
                # SE TIVER CÃES NA LISTA EXECUTA ESSE BLOCO, SENÃO PULA PRO ELSE
                    cao_parceiro = int(input("Digite o cão que deseja fazer o cruzamento \n"))
                    if cao_parceiro in range(0, len(lista_cruzamento)):
                        lista_caes[cao_atual].pode_cruzar(lista_cruzamento[cao_parceiro])
                        filhotes = lista_caes[cao_atual].cruzar(lista_cruzamento[cao_parceiro])
                        print("O CRUZAMENTO ENTRE {} E {} RESULTOU EM {} FILHOTES, PARABÉNS \n".format(lista_caes[cao_atual].nome, lista_cruzamento[cao_parceiro].nome, filhotes))
                    else:
                        print("Opção Inválida")
                else:
                    print("NÃO TEM CÃES DISPONÍVEIS")
            elif opcao == 5:
                print("Voltando ao menu inicial... \n")
            else:
                print("Opção Inválida")
    except ValueError:
        print("Digite algo válido")

def main():
    opcao = 0
    lista_caes = []
    print("SEJA BEM VINDO AO ADMINISTRADOR DE CÃES! \n")
    while opcao != 3:
        try:
            opcao = int(input("ESCOLHA UMA DAS OPÇÕES ABAIXO \n1) Cadastrar cão \n2) Listar cães \n3) Sair do programa \n"))
            if opcao == 1:
                nome = input("Digite o nome do Cão \n").upper()
                raca = input("Digite a raça do Cão \n").upper()
                sexo = input("Digite o sexo do Cão (M OU F)\n").upper()
                idade = int(input("Digite a idade do Cão \n"))
                lista_caes.append(Cachorro(nome, raca, sexo, idade))
            elif opcao == 2:
                print("Lista de Cães")
                if len(lista_caes) > 0:
                    for i in range(0, len(lista_caes)):
                        print("CÃO Nº {}: {}\n".format(i, lista_caes[i].nome))
                    cao_atual = int(input("Digite o cão que deseja escolher: \n"))
                    if cao_atual in range(0, len(lista_caes)): manipular_cachorro(cao_atual, lista_caes)
                    else: print("Cão Inválido")
                else:
                    print("Não existem cães cadastrados")
            elif opcao == 3:
                exit(0)
            else:
                print("Opção Inválida")
        except ValueError:
            print("Digite algo válido")

# TESTA QUAL ARQUIVO FOI INICIALIZADO PRIMEIRO
if __name__ == "__main__": main()