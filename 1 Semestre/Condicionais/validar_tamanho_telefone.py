def verificar_quantidade_caracteres(mensagem):

    valor = input(mensagem)

    qtd_caracteres_telefone = len(valor)

    return (qtd_caracteres_telefone < 8) or (qtd_caracteres_telefone > 11)

def gerador_textos(valido):
    if not valido:
        print("Inválido")
    else:
        print("Válido")

def main():
    telefone_valido = verificar_quantidade_caracteres("Digite um número de telefone: ")

    print(f"Seu telefone tem {qtd_caracteres_telefone} números")

    verificar_quantidade_caracteres(telefone_valido)


# telefone = input("Digite um número de telefone: ")

# def verificar_quantidade_caracteres(telefone):
#     qtd_caracteres_telefone = len(telefone)
#     if (qtd_caracteres_telefone < 8 or qtd_caracteres_telefone > 11):
#         print("Incorreto")
#     else:
#         print("Correto")
#     print(f"Seu telefone tem {qtd_caracteres_telefone} números")

# verificar_quantidade_caracteres(telefone)