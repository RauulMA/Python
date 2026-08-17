def soma(lista):
    resposta = 0
    for el in lista:
        resposta = resposta + el
    return resposta


def media(lista):
    somado = soma(lista)
    tamanho = len(lista)
    return somado/tamanho


assert media([2,3,4]) == 3
print(media([2,3,4]))