from enum import Enum

IDADE_MINIMA_HOMEM = 65
CONTRIBUICAO_MINIMA_HOMEM = 15
IDADE_MINIMA_MULHER = 62
CONTRIBUICAO_MINIMA_MULHER = 12

class Sexo(Enum):
    MASCULINO = 1
    FEMININO = 2

def pode_aposentar(idade: int, sexo: int, contribuicao: int) -> list:
    if sexo == Sexo.MASCULINO:
        return gerar_aposentadoria(idade >= IDADE_MINIMA_HOMEM, contribuicao >= CONTRIBUICAO_MINIMA_HOMEM)
    else:
        return gerar_aposentadoria(idade >= IDADE_MINIMA_MULHER, contribuicao >= CONTRIBUICAO_MINIMA_MULHER)

def gerar_aposentadoria(idade: bool, contribuicao: bool) -> list:
    texto = []
    if not idade:
        texto.append("Não pode aposentar por idade.")
    if not contribuicao:
        texto.append("Não pode aposentar por contribuição.")
    if idade and contribuicao:
        texto.append("Pode aposentar.")
    return texto
    
def verificar_valor_positivo(mensagem: str) -> int:
    while True:
        try:
            valor = int(input(mensagem))
            if valor <= 0:
                print("Digite um valor maior que 0.")
                continue
            return valor
        except ValueError:
            print("Digite um número.")

def verificar_valor_sexo(mensagem: str) -> int:
    while True:
        try:
            valor = int(input(mensagem))
            if valor not in [1, 2]:
                print("Digite 1 ou 2.")
                continue
            return valor
        except ValueError:
            print("Digite um número.")

def main():
    idade = verificar_valor_positivo("Digite sua idade: ")
    sexo = Sexo(verificar_valor_sexo("1-Masculino\n2-Feminino\nDigite seu sexo: "))
    contribuicao = verificar_valor_positivo("Digite a quantidade de anos de contribuição: ")
    resultados = pode_aposentar(idade, sexo, contribuicao)
    for resultado in resultados:
        print(resultado)

if __name__ == "__main__":
    main()

#Função log