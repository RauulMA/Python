from enum import Enum

class Opcoes(Enum):
    PRIMEIRO_ITEM_LISTA = 1
    ULTIMO_ITEM_LISTA = 2
    MAIOR_ITEM_LISTA = 3

lista = [0, 1, 4, 3]

def verificar_resposta(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            if valor not in [1, 2, 3]:
                print("Digite um número aceitável.")
            return valor
        except ValueError:
            print("Digite um número.")

def retornar_solicitacao(valor):
    maior = 0.0
    if valor == Opcoes.PRIMEIRO_ITEM_LISTA:
        return f"Primeiro item da lista: {lista[0]}"
    elif valor == Opcoes.ULTIMO_ITEM_LISTA:
        return f"Último item da lista: {lista[-1]}"
    elif valor == Opcoes.MAIOR_ITEM_LISTA:
        for x in lista: 
            if x >= maior:
                maior = x
        return f"\nO maior número é o {maior}"
    
def main():
    resposta = Opcoes(verificar_resposta(f"Itens da lista: {lista}\n\n1-Localizar o primeiro item da lista\n2-Localizar o último item da lista\n3-Localizar o maior item da lista\n\nDigite qual função você quer realizar: "))
    print(retornar_solicitacao(resposta))

if __name__ == "__main__":
    main()