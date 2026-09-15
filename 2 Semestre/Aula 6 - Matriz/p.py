def lugares_livres(sala):
    pol_livres = 0
    #return sum([len([pol_livres+1 for count in range(len(poltronas)) if poltronas[count] == '_']) for poltronas in sala])
    return sum(1 for fileira in sala for lugar in fileira if lugar == '_')

def livres_na_fila(sala, fila):
    return lugares_livres(sala[fila])

def fila_mais_vazia(sala):
    sala_mais_vazia = 0
    for x in range(len(sala)):
        if livres_na_fila(sala, x) > sala_mais_vazia:
            sala_mais_vazia = x
    return sala_mais_vazia
    return [sala_mais_vazia for x in range(len(sala)) if livres_na_fila(sala, x) > sala_mais_vazia]

print(lugares_livres([['_', 'X'], ['_', '_']]))
#print(fila_mais_vazia([['_', 'X'], ['_', '_']]))