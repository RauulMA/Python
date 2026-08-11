def encontrar_elemento(lista: list, item: int) -> bool:
    for x in lista:
        if item == x:
            return True
        
def verificar_valor(mensagem: str) -> int:
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print("Digite um número.\n")

def realizar_busca(lista: list, item: int) -> str:
    if encontrar_elemento(lista, item):
        print("Elemento encontrado.")
    else:
        print("Não encontrado.")

def main():
    lista = [1, 2, 3, 4, 5]
    valor = verificar_valor("Digite um número que pode estar na lista: ")
    realizar_busca(lista, valor)

if __name__ == "__main__":
    main()