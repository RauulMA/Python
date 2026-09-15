import tracemalloc
import gc

def lugares_livres(sala):
    pol_livres = 0
    for pol in sala:
       for c in range(len(pol)):
           if pol[c] == '_':
               pol_livres+=1
    return pol_livres

def lugares_livres_original(sala):
    pol_livres = 0

    return sum([
        len([
            pol_livres + 1
            for c in range(len(pol))
            if pol[c] == '_'
        ])
        for pol in sala
    ])

def lugares_livres_gerador(sala):
    return sum(
        1
        for fileira in sala
        for lugar in fileira
        if lugar == '_'
    )


def medir_memoria(funcao, sala):
    gc.collect()

    tracemalloc.start()

    resultado = funcao(sala)

    memoria_atual, pico = tracemalloc.get_traced_memory()

    tracemalloc.stop()

    return resultado, memoria_atual, pico

sala = [
    ['_', 'X', '_', '_', 'X'] * 10000
    for _ in range(10000)
]

resultado0, atual0, pico0 = medir_memoria(
    lugares_livres,
    sala
)

resultado1, atual1, pico1 = medir_memoria(
    lugares_livres_original,
    sala
)

resultado2, atual2, pico2 = medir_memoria(
    lugares_livres_gerador,
    sala
)

print("Versão com for padrão:")
print(f"Resultado: {resultado0}")
print(f"Memória atual: {atual0 / 1024:.2f} KiB")
print(f"Pico de memória: {pico0 / 1024:.2f} KiB")

print("\nVersão com list comprehenson:")
print(f"Resultado: {resultado1}")
print(f"Memória atual: {atual1 / 1024:.2f} KiB")
print(f"Pico de memória: {pico1 / 1024:.2f} KiB")

print("\nVersão com sum:")
print(f"Resultado: {resultado2}")
print(f"Memória atual: {atual2 / 1024:.2f} KiB")
print(f"Pico de memória: {pico2 / 1024:.2f} KiB")