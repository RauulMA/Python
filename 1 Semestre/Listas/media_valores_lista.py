def verificar_valor(mensagem: str) -> float:
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Digite um número.\n")

def calcular_media(valores: list[float]) -> float:
    if not valores:
        return 0.0
    return sum(valores) / len(valores)

def solicitar_valores(notas: int) -> list[float]:
    valores = []
    for x in range(1, notas+1):
        valores.append(verificar_valor(f"Digite o {x}º valor: "))
    return valores

def main():
    notas = int(verificar_valor("Digite a quantidade de notas a serem calculadas: "))
    print(f"\nA média é de {calcular_media(solicitar_valores(notas)):.2f}")

if __name__ == "__main__":
    main()