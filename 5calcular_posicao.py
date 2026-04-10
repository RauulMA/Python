def verificar_valor_positivo(mensagem: str) -> float:
    while True:
        try:
            valor = float(input(mensagem))
            if valor < 0:
                print("Digite um valor maior que zero.")
                continue
            return valor
        except ValueError:
            print("Digite um valor numérico.")

def calcular_posicao_futura(velocidade: float, posicao: float, tempo: int) -> float:
    return velocidade * tempo + posicao

def exibir_posicao_futura(posicao_futura: float) -> str:
    return f"Após duas horas, sua posição será de {posicao_futura} quilômetros"

def main():
    velocidade = verificar_valor_positivo("Digite sua velocidade: ")
    km_atual = verificar_valor_positivo("Digite o quilômetro em que você está localizado: ")

    print(exibir_posicao_futura(calcular_posicao_futura(velocidade, km_atual, 2)))

if __name__ == "__main__":
    main()