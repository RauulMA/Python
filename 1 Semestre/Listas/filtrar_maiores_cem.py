class Limites():
    LIMITE_CEM = 100

def verificar_valor(mensagem: str) -> int:
    while True:
        try:
            valor = int(input(mensagem))
            if valor <= 0:
                print("Digite um número maior que zero.\n")
                continue
            return valor
        except ValueError:
            print("Digite um número.\n")

def verificar_valor_lista(mensagem: str) -> int:
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print("Digite um número.\n")

def maiores_cem(lista: list) -> list:
    return [x for x in lista if x > Limites.LIMITE_CEM]

def receber_itens_lista(vezes: int, lista: list) -> list:
    for x in range(vezes):
        lista.append(verificar_valor_lista(f"Digite o {x}º número: "))
    return maiores_cem(lista)

def main():
    lista = []
    vezes = verificar_valor("Digite a quantidade de números a serem inseridos na lista: ")
    print(f"Os valores maiores que {Limites.LIMITE_CEM} são: {receber_itens_lista(vezes, lista)}")

if __name__ == "__main__":
    main()