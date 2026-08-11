def verificar_valor_positivo(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            if valor <= 0:
                print("Digite um valor maior que zero.")
                continue
            return valor
        except ValueError:
            print("Digite um valor numérico.")

def verificar_questionamento_aniversario(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            if (valor != 1) and (valor != 2):
                print("Digite 1 ou 2.")
                continue
            return valor
        except ValueError:
            print("Digite um valor numérico.")
    
def calcular_idade(nascimento, ano_atual):
    return ano_atual - nascimento

def verificar_fez_aniversario(aniversario, idade):
    if aniversario == 2:
        idade-=1
    return idade

def main():
    ano_nascimento = verificar_valor_positivo("Digite seu ano de nascimento: ")
    ano_atual = verificar_valor_positivo("Digite em que ano estamos: ")
    fez_aniversario = verificar_questionamento_aniversario("Fez aniversário?\n1-Sim\n2-Não\nDigite se fez aniversário: ")

    print(f"Sua idade é de {verificar_fez_aniversario(fez_aniversario, calcular_idade(ano_nascimento, ano_atual))} anos")

if __name__ == "__main__":
    main()