def verificar_valor(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except ValueError:
            print("Digite um número.\n")

def calcular_media(*args):
    media = 0.0
    for arg in args:
        media += arg
    return media / len(args)

def main():
    valor1 = verificar_valor("Digite um valor: ")
    valor2 = verificar_valor("Digite outro valor: ")
    valor3 = verificar_valor("Digite um outro valor: ")

    print(f"A média é de {calcular_media(valor1, valor2, valor3)}")

if __name__ == "__main__":
    main()


#-------------------------------------------------------------------------------

# def calcular_media(*args):
#     media = 0.0
#     for arg in args:
#         media += arg
#     return media / len(args)

# valor1 = float(input(f"Digite o 1º valor: "))
# valor2 = float(input(f"Digite o 2º valor: "))
# valor3 = float(input(f"Digite o 3º valor: "))

# print(f"A média é de {calcular_media(valor1, valor2, valor3)}")

#-------------------------------------------------------------------------------

# media = 0.0

# for x in range(1,4):
#     valor = float(input(f"Digite o {x}º valor: "))
#     media =  media + valor
#     if x == 3:
#         media = media / x

# print(f"A média é de {media}")

#-------------------------------------------------------------------------------

# valor1 = float(input("Digite um valor: "))
# valor2 = float(input("Digite um valor: "))
# valor3 = float(input("Digite um valor: "))

# media = (valor1+valor2+valor3)/3

# print(f"A média de {valor1}, {valor2} e {valor3} é de {media}")