def verificar_valor_segundos_positivo(mensagem):
    while True:
        try:
            segundos_formatados = int(input(mensagem))
            if segundos_formatados < 0:
                print(print("O valor deve ser positivo."))
                continue
            return segundos_formatados
        except ValueError:
            print(print("O valor deve ser um número."))
        
def calcular_minutos(segundo):
    minutos = segundo // 60 - calcular_horas (segundo)*60
    return minutos

def calcular_horas(segundo):
    horas = segundo // 3600
    return horas

def calcular_segundos(segundo):
    segundo = segundo % 60
    return segundo

def main():
        segundos = verificar_valor_segundos_positivo("Digite uma quantidade de segundos: ")
        print(f"Isso dá {calcular_horas(segundos)}h {calcular_minutos(segundos)}min {calcular_segundos(segundos)}segs")

if __name__ == "__main__":
    main()