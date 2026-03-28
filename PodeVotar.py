
# nota = verificar_valor_positivo("Digite sua nota: ")
# presenca = verificar_valor_positivo("Digite sua presenca: ")

# passou = presenca >= 75 and nota >= 6
# exame = presenca >= 75 and (nota >= 4 and nota <= 6)

# print(f"Seu resultado:\nVocê passou: {passou}\nVocê pode fazer o exame para passar: {exame}")

def verificar_valor_positivo(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor < 0:
                print("Valor incorreto.")
                continue
            return valor
        except ValueError:
            print("caracter incorreto.")

def calcular_criterios(nota, presenca):
    passou = presenca >= 75 and nota >= 6
    exame = presenca >= 75 and (4 <= nota <= 6)
    reprovado = not passou and not exame
    Texto_final = print(f"Seu resultado:\nVocê passou: {passou}\nVocê pode fazer o exame para passar: {exame}\nVocê foi reprovado: {reprovado}")
    return Texto_final

def main():
    nota = verificar_valor_positivo("Digite sua nota: ")
    presenca = verificar_valor_positivo("Digite sua presenca: ")

    calcular_criterios(nota, presenca)

if __name__ == "__main__":
    main()