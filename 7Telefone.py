telefone = input("Digite um número de telefone: ")

def verificar_quantidade_caracteres(telefone):

    qtd_caracteres_telefone = len(telefone)

    return (qtd_caracteres_telefone < 8) or (qtd_caracteres_telefone > 11)

    print(f"Seu telefone tem {qtd_caracteres_telefone} números")

verificar_quantidade_caracteres(telefone)


telefone = input("Digite um número de telefone: ")

def verificar_quantidade_caracteres(telefone):
    qtd_caracteres_telefone = len(telefone)
    if (qtd_caracteres_telefone < 8 or qtd_caracteres_telefone > 11):
        print("Incorreto")
    else:
        print("Correto")
    print(f"Seu telefone tem {qtd_caracteres_telefone} números")

verificar_quantidade_caracteres(telefone)