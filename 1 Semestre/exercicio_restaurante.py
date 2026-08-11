
# === Boilerplate (pode ignorar) ===
# Esse codigo so serve para o professor testar o gabarito em casa. Voce nao precisa dele. Pode ignorar ou deletar
import hashlib
def verifica(valor, codigo):
    assert hashlib.sha224(str(valor).encode('utf-8')).hexdigest() == codigo, f'Valor errado: voce colocou {valor}'

try:
    import gabarito_NAO_MANDAR as _gab
    _GAB = {k: v for k, v in vars(_gab).items() if not k.startswith('_')}
except ImportError:
    _GAB = {}

def _aplica(nome):
    if nome in _GAB:
        globals()[nome] = _GAB[nome]
# fim do boilerplate


'''
EXPLICACAO

Bem-vindo ao exercicio do restaurante! Aqui vamos praticar listas em Python.

Lembrando: uma lista guarda varios valores em ordem. Cada valor tem uma
posicao (chamada de "indice"), comecando do 0.

    > frutas = ["maca", "banana", "uva"]
    > frutas[0]
    'maca'
    > frutas[1]
    'banana'
    > frutas[2]
    'uva'

Para saber quantos elementos tem na lista, usamos len():

    > len(frutas)
    3

Para adicionar um elemento no fim da lista, usamos .append():

    > frutas.append("manga")
    > frutas
    ['maca', 'banana', 'uva', 'manga']
    > len(frutas)
    4
'''


# ===== FASE 1 - Revisao de listas =====

'''
EXERCICIO

Considere a lista a seguir:
    frutas = ["maca", "banana", "uva", "manga"]

Lembrando que as posicoes (indices) comecam do 0, responda as perguntas
preenchendo as variaveis abaixo. Coloque os valores como string (entre
aspas), por exemplo "maca".

1) Qual a fruta na posicao 0?
'''
fruta_pos_0 = 'coloque o valor aqui'

'''
2) Qual a fruta na posicao 2?
'''
fruta_pos_2 = 'coloque o valor aqui'

'''
3) Qual a fruta na posicao 3?
'''
fruta_pos_3 = 'coloque o valor aqui'

_aplica('fruta_pos_0'); _aplica('fruta_pos_2'); _aplica('fruta_pos_3') #essa linha só serve para o professor testar o exercicio em casa. Pode ignorar ou deletar

import hashlib
def verifica(valor, codigo):
    assert hashlib.sha224(str(valor).encode('utf-8')).hexdigest() == codigo, f'Valor errado: voce colocou {valor}'

verifica(fruta_pos_0, '041d97650b3549cded949238c52e7f87abcc5921dfe7e0a3f4166172')
verifica(fruta_pos_2, 'a1abe6b14f7465d1709876648df0468c28cb21415eaec7d42adf660f')
verifica(fruta_pos_3, 'ac471e3f8fe6557319200610e4f2376d936fbae9cc172db87c223e4a')
print('Exercicio acesso por indice: OK')


'''
EXERCICIO

Ainda considerando a lista:
    frutas = ["maca", "banana", "uva", "manga"]

Quantos elementos tem essa lista? (Pode usar len() na sua cabeca,
ou contar.) Coloque o valor como numero, nao como string.
'''
tamanho_frutas = 'coloque o valor aqui'

_aplica('tamanho_frutas') #essa linha só serve para o professor testar o exercicio em casa. Pode ignorar ou deletar

verifica(tamanho_frutas, '271f93f45e9b4067327ed5c8cd30a034730aaace4382803c3e1d6c2f')
print('Exercicio tamanho da lista: OK')


# ===== FASE 2 - Listas paralelas =====

'''
EXPLICACAO

Agora vamos para o conceito principal desse exercicio: LISTAS PARALELAS.

Imagine que queremos guardar produtos de um restaurante e seus precos.
Uma forma simples e usar DUAS listas, onde a posicao i de uma corresponde
a posicao i da outra. Por exemplo:

    nomes  = ["pizza", "suco", "salada", "agua"]
    precos = [25,      8,      15,       5     ]

Ou seja:
    - "pizza" esta na posicao 0 de nomes; seu preco (25) esta na posicao 0 de precos
    - "suco"  esta na posicao 1 de nomes; seu preco (8)  esta na posicao 1 de precos
    - "salada" esta na posicao 2 de nomes; seu preco (15) esta na posicao 2 de precos
    - "agua"  esta na posicao 3 de nomes; seu preco (5)  esta na posicao 3 de precos

Se eu quero saber o preco da pizza:
    1) Acho a posicao da "pizza" em nomes -> posicao 0
    2) Olho precos[0] -> 25

Esse padrao (duas listas que se correspondem por indice) e bem comum em
programacao quando estamos comecando.
'''

'''
EXERCICIO

Considere as listas a seguir:
    nomes  = ["pizza", "suco", "salada", "agua"]
    precos = [25,      8,      15,       5     ]

Responda as perguntas. Coloque os valores como numero.

1) Qual o preco da pizza?
'''
preco_da_pizza = 'coloque o valor aqui'

'''
2) Qual o preco da salada?
'''
preco_da_salada = 'coloque o valor aqui'

'''
3) Qual o preco da agua?
'''
preco_da_agua = 'coloque o valor aqui'

_aplica('preco_da_pizza'); _aplica('preco_da_salada'); _aplica('preco_da_agua') #essa linha só serve para o professor testar o exercicio em casa. Pode ignorar ou deletar

verifica(preco_da_pizza, '76b8d44676fed57eb0e3627eff69165c9ea9788ad0e832560d48a146')
verifica(preco_da_salada, '87592c38e2b36a1d35437714ecedee4d6fad7a1a0b1bf5d7a2ab68ef')
verifica(preco_da_agua, 'b51d18b551043c1f145f22dbde6f8531faeaf68c54ed9dd79ce24d17')
print('Exercicio listas paralelas: OK')


'''
EXERCICIO

Faca uma funcao acha_indice(lista, item) que percorre a lista procurando
pelo item, e retorna o indice (a posicao) onde ele esta. Voce pode assumir
que o item esta na lista.

Dica: use um for, e uma variavel i que comeca em 0 e vai
incrementando ate encontrar o item.

    >>> acha_indice(["maca", "banana", "uva"], "banana")
    1
    >>> acha_indice(["pizza", "suco", "salada"], "salada")
    2
    >>> acha_indice([10, 20, 30, 40], 30)
    2
'''
def acha_indice(lista, item):
    pass
_aplica('acha_indice') #essa linha só serve para o professor testar o exercicio em casa. Pode ignorar ou deletar

assert acha_indice(["maca", "banana", "uva"], "banana") == 1, 'acha_indice("banana") deveria ser 1'
assert acha_indice(["maca", "banana", "uva"], "maca") == 0, 'acha_indice("maca") deveria ser 0'
assert acha_indice(["maca", "banana", "uva"], "uva") == 2, 'acha_indice("uva") deveria ser 2'
assert acha_indice([10, 20, 30, 40], 30) == 2, 'acha_indice(30) deveria ser 2'
assert acha_indice([10, 20, 30, 40], 10) == 0, 'acha_indice(10) deveria ser 0'
print('Exercicio acha_indice: OK')


# ===== FASE 3 - As funcoes do restaurante =====

'''
EXPLICACAO

Agora vamos implementar o sistema do restaurante!

Os produtos vao ser guardados em duas listas paralelas, declaradas
no nivel do arquivo (fora de qualquer funcao):

    nomes = []
    precos = []

As proximas funcoes vao MODIFICAR essas listas, ou ler delas.
'''

# As listas globais do restaurante. Comecam vazias.
nomes = []
precos = []
_aplica('nomes'); _aplica('precos') #essa linha só serve para o professor testar o exercicio em casa. Pode ignorar ou deletar


'''
EXERCICIO

Faca uma funcao cadastra(nome, preco) que adiciona um produto novo
ao restaurante. Ela deve:
    - adicionar o nome no fim da lista nomes
    - adicionar o preco no fim da lista precos

A funcao nao precisa retornar nada.

    >>> nomes  -> []
    >>> precos -> []
    >>> cadastra("pizza", 25)
    >>> nomes  -> ["pizza"]
    >>> precos -> [25]
    >>> cadastra("suco", 8)
    >>> nomes  -> ["pizza", "suco"]
    >>> precos -> [25, 8]
'''
def cadastra(nome, preco):
    pass
_aplica('cadastra') #essa linha só serve para o professor testar o exercicio em casa. Pode ignorar ou deletar

# reset das listas globais antes de testar
nomes.clear(); precos.clear()
cadastra("pizza", 25)
assert nomes == ["pizza"], f'Apos cadastra("pizza", 25), nomes deveria ser ["pizza"], obteve {nomes}'
assert precos == [25], f'Apos cadastra("pizza", 25), precos deveria ser [25], obteve {precos}'
cadastra("suco", 8)
assert nomes == ["pizza", "suco"], f'Apos cadastra("suco", 8), nomes deveria ser ["pizza", "suco"], obteve {nomes}'
assert precos == [25, 8], f'Apos cadastra("suco", 8), precos deveria ser [25, 8], obteve {precos}'
cadastra("salada", 15)
assert nomes == ["pizza", "suco", "salada"], f'nomes errado: {nomes}'
assert precos == [25, 8, 15], f'precos errado: {precos}'
print('Exercicio cadastra: OK')


'''
EXERCICIO

Faca uma funcao preco_de(nome) que retorna o preco de um produto pelo nome.

Dica: use a funcao acha_indice que voce ja fez para achar a posicao do
nome em nomes, e depois pegue precos[posicao].

Voce pode assumir que o produto esta cadastrado.

    >>> nomes  -> ["pizza", "suco", "salada"]
    >>> precos -> [25, 8, 15]
    >>> preco_de("pizza")
    25
    >>> preco_de("suco")
    8
    >>> preco_de("salada")
    15
'''
def preco_de(nome):
    pass
_aplica('preco_de') #essa linha só serve para o professor testar o exercicio em casa. Pode ignorar ou deletar

# reset e cadastro de produtos conhecidos
nomes.clear(); precos.clear()
cadastra("pizza", 25)
cadastra("suco", 8)
cadastra("salada", 15)
cadastra("agua", 5)

assert preco_de("pizza") == 25, f'preco_de("pizza") deveria ser 25, obteve {preco_de("pizza")}'
assert preco_de("suco") == 8, f'preco_de("suco") deveria ser 8, obteve {preco_de("suco")}'
assert preco_de("salada") == 15, f'preco_de("salada") deveria ser 15, obteve {preco_de("salada")}'
assert preco_de("agua") == 5, f'preco_de("agua") deveria ser 5, obteve {preco_de("agua")}'
print('Exercicio preco_de: OK')


'''
EXERCICIO

Faca uma funcao muda_preco(nome, novo_preco) que muda o preco de um
produto ja cadastrado.

Dica: ache a posicao do nome em nomes, e atribua o novo preco em
precos[posicao].

Voce pode assumir que o produto esta cadastrado. A funcao nao precisa
retornar nada.

    >>> nomes  -> ["pizza", "suco", "salada"]
    >>> precos -> [25, 8, 15]
    >>> muda_preco("suco", 10)
    >>> precos
    [25, 10, 15]
    >>> muda_preco("pizza", 30)
    >>> precos
    [30, 10, 15]
'''
def muda_preco(nome, novo_preco):
    pass
_aplica('muda_preco') #essa linha só serve para o professor testar o exercicio em casa. Pode ignorar ou deletar

# reset
nomes.clear(); precos.clear()
cadastra("pizza", 25)
cadastra("suco", 8)
cadastra("salada", 15)

muda_preco("suco", 10)
assert precos == [25, 10, 15], f'Apos muda_preco("suco", 10), precos deveria ser [25, 10, 15], obteve {precos}'
muda_preco("pizza", 30)
assert precos == [30, 10, 15], f'Apos muda_preco("pizza", 30), precos deveria ser [30, 10, 15], obteve {precos}'
muda_preco("salada", 20)
assert precos == [30, 10, 20], f'precos errado: {precos}'
# nomes nao deve ter mudado
assert nomes == ["pizza", "suco", "salada"], f'muda_preco nao deveria alterar nomes, mas nomes ficou {nomes}'
print('Exercicio muda_preco: OK')


'''
EXERCICIO

Faca uma funcao total_pedido(pedido) que recebe uma lista de nomes de
produtos (um pedido) e retorna o preco total - a soma dos precos de
todos os produtos do pedido.

Dica: use um for ou while para percorrer o pedido. Para cada nome,
some o resultado de preco_de(nome) numa variavel total.

    >>> nomes  -> ["pizza", "suco", "salada", "agua"]
    >>> precos -> [25, 8, 15, 5]
    >>> total_pedido(["pizza", "suco"])
    33
    >>> total_pedido(["salada"])
    15
    >>> total_pedido(["pizza", "pizza", "agua"])
    55
'''
def total_pedido(pedido):
    pass
_aplica('total_pedido') #essa linha só serve para o professor testar o exercicio em casa. Pode ignorar ou deletar

# reset
nomes.clear(); precos.clear()
cadastra("pizza", 25)
cadastra("suco", 8)
cadastra("salada", 15)
cadastra("agua", 5)

assert total_pedido(["pizza", "suco"]) == 33, f'total_pedido(["pizza", "suco"]) deveria ser 33, obteve {total_pedido(["pizza", "suco"])}'
assert total_pedido(["salada"]) == 15, f'total_pedido(["salada"]) deveria ser 15, obteve {total_pedido(["salada"])}'
assert total_pedido(["pizza", "pizza", "agua"]) == 55, f'total_pedido(["pizza", "pizza", "agua"]) deveria ser 55, obteve {total_pedido(["pizza", "pizza", "agua"])}'
assert total_pedido([]) == 0, f'total_pedido([]) deveria ser 0 (pedido vazio), obteve {total_pedido([])}'
print('Exercicio total_pedido: OK')


# ===== FASE 4 - Gerenciando os pedidos do dia =====

'''
EXPLICACAO

Agora vamos representar TODOS os pedidos do restaurante no dia.

Cada pedido e uma lista de produtos (ja vimos isso na funcao total_pedido).
A novidade: vamos guardar todos os pedidos do dia em mais uma lista. Ou seja,
vamos ter uma LISTA DE LISTAS:

    pedidos = [
        ["pizza", "suco"],     # pedido 0
        ["salada"],            # pedido 1
        ["pizza", "pizza"],    # pedido 2
    ]

Para acessar o pedido 0 inteiro:
    > pedidos[0]
    ['pizza', 'suco']

Para adicionar um produto ao pedido 0:
    > pedidos[0].append("agua")
    > pedidos[0]
    ['pizza', 'suco', 'agua']

Tambem vamos usar um metodo novo de listas: .remove(item), que remove a
PRIMEIRA ocorrencia do item da lista.

    > frutas = ["maca", "banana", "uva", "banana"]
    > frutas.remove("banana")
    > frutas
    ['maca', 'uva', 'banana']
'''

# A lista global de pedidos do dia. Comeca vazia.
pedidos = []
_aplica('pedidos') #essa linha só serve para o professor testar o exercicio em casa. Pode ignorar ou deletar


'''
EXERCICIO

Faca uma funcao cria_pedido() que cria um novo pedido VAZIO no
restaurante. Ela deve:
    - adicionar uma lista vazia [] no fim da lista pedidos
    - retornar o indice do pedido recem-criado

Dica: o indice do pedido recem-criado e o tamanho da lista MENOS 1
(pois indices comecam do 0).

    >>> pedidos -> []
    >>> cria_pedido()
    0
    >>> pedidos -> [[]]
    >>> cria_pedido()
    1
    >>> pedidos -> [[], []]
'''
def cria_pedido():
    pass
_aplica('cria_pedido') #essa linha só serve para o professor testar o exercicio em casa. Pode ignorar ou deletar

# reset
pedidos.clear()
assert cria_pedido() == 0, 'primeiro cria_pedido deveria retornar 0'
assert pedidos == [[]], f'pedidos deveria ser [[]], obteve {pedidos}'
assert cria_pedido() == 1, 'segundo cria_pedido deveria retornar 1'
assert pedidos == [[], []], f'pedidos deveria ser [[], []], obteve {pedidos}'
assert cria_pedido() == 2, 'terceiro cria_pedido deveria retornar 2'
assert pedidos == [[], [], []], f'pedidos deveria ser [[], [], []], obteve {pedidos}'
print('Exercicio cria_pedido: OK')


'''
EXERCICIO

Faca uma funcao adiciona_ao_pedido(indice, produto) que adiciona um
produto ao pedido na posicao indice.

Dica: use append no pedido certo: pedidos[indice].append(produto).

A funcao nao precisa retornar nada.

    >>> pedidos -> [[], []]
    >>> adiciona_ao_pedido(0, "pizza")
    >>> pedidos -> [["pizza"], []]
    >>> adiciona_ao_pedido(0, "suco")
    >>> pedidos -> [["pizza", "suco"], []]
    >>> adiciona_ao_pedido(1, "salada")
    >>> pedidos -> [["pizza", "suco"], ["salada"]]
'''
def adiciona_ao_pedido(indice, produto):
    pass
_aplica('adiciona_ao_pedido') #essa linha só serve para o professor testar o exercicio em casa. Pode ignorar ou deletar

# reset
pedidos.clear()
cria_pedido()  # pedido 0
cria_pedido()  # pedido 1

adiciona_ao_pedido(0, "pizza")
assert pedidos == [["pizza"], []], f'pedidos errado: {pedidos}'
adiciona_ao_pedido(0, "suco")
assert pedidos == [["pizza", "suco"], []], f'pedidos errado: {pedidos}'
adiciona_ao_pedido(1, "salada")
assert pedidos == [["pizza", "suco"], ["salada"]], f'pedidos errado: {pedidos}'
adiciona_ao_pedido(1, "agua")
assert pedidos == [["pizza", "suco"], ["salada", "agua"]], f'pedidos errado: {pedidos}'
print('Exercicio adiciona_ao_pedido: OK')


'''
EXERCICIO

Faca uma funcao remove_do_pedido(indice, produto) que remove um
produto (a primeira ocorrencia) do pedido na posicao indice.

Dica: use o metodo .remove(): pedidos[indice].remove(produto).

A funcao nao precisa retornar nada. Voce pode assumir que o produto
esta no pedido.

    >>> pedidos -> [["pizza", "suco", "pizza"], ["salada"]]
    >>> remove_do_pedido(0, "pizza")
    >>> pedidos -> [["suco", "pizza"], ["salada"]]
    (note: removeu so a PRIMEIRA pizza, a segunda continuou)
    >>> remove_do_pedido(1, "salada")
    >>> pedidos -> [["suco", "pizza"], []]
'''
def remove_do_pedido(indice, produto):
    pass
_aplica('remove_do_pedido') #essa linha só serve para o professor testar o exercicio em casa. Pode ignorar ou deletar

# reset
pedidos.clear()
cria_pedido()
cria_pedido()
adiciona_ao_pedido(0, "pizza")
adiciona_ao_pedido(0, "suco")
adiciona_ao_pedido(0, "pizza")
adiciona_ao_pedido(1, "salada")
# pedidos = [["pizza", "suco", "pizza"], ["salada"]]

remove_do_pedido(0, "pizza")
assert pedidos == [["suco", "pizza"], ["salada"]], f'remove_do_pedido(0, "pizza") deveria deixar [["suco", "pizza"], ["salada"]], obteve {pedidos}'
remove_do_pedido(1, "salada")
assert pedidos == [["suco", "pizza"], []], f'pedidos errado: {pedidos}'
remove_do_pedido(0, "suco")
assert pedidos == [["pizza"], []], f'pedidos errado: {pedidos}'
print('Exercicio remove_do_pedido: OK')


'''
EXERCICIO

Para fechar o caixa do restaurante no final do dia, faca uma funcao
receita_do_dia() (sem parametros!) que retorna a receita total do dia.

Use a lista global pedidos. Para cada pedido nela, some o
total_pedido(pedido) numa variavel receita.

    >>> nomes  -> ["pizza", "suco", "salada", "agua"]
    >>> precos -> [25, 8, 15, 5]
    >>> pedidos -> [["pizza", "suco"], ["salada"], ["pizza"]]
    >>> receita_do_dia()
    73
    (porque 33 + 15 + 25 = 73)
'''
def receita_do_dia():
    pass
_aplica('receita_do_dia') #essa linha só serve para o professor testar o exercicio em casa. Pode ignorar ou deletar

# reset completo: produtos cadastrados e lista de pedidos
nomes.clear(); precos.clear()
cadastra("pizza", 25)
cadastra("suco", 8)
cadastra("salada", 15)
cadastra("agua", 5)
pedidos.clear()

# sem pedidos -> receita 0
assert receita_do_dia() == 0, 'receita do dia sem pedidos deveria ser 0'

# 3 pedidos: 33 + 15 + 25 = 73
cria_pedido(); adiciona_ao_pedido(0, "pizza"); adiciona_ao_pedido(0, "suco")
cria_pedido(); adiciona_ao_pedido(1, "salada")
cria_pedido(); adiciona_ao_pedido(2, "pizza")
assert receita_do_dia() == 73, f'receita errada: esperado 73, obteve {receita_do_dia()}'

# adicionar uma agua ao pedido 1: 33 + 20 + 25 = 78
adiciona_ao_pedido(1, "agua")
assert receita_do_dia() == 78, f'receita errada: esperado 78, obteve {receita_do_dia()}'

# remover suco do pedido 0: 25 + 20 + 25 = 70
remove_do_pedido(0, "suco")
assert receita_do_dia() == 70, f'receita errada: esperado 70, obteve {receita_do_dia()}'

print('Exercicio receita_do_dia: OK')


print('\n=== PARABENS! Todos os exercicios completos! ===')


# ===== INTERFACE CLI DO RESTAURANTE =====
#
# Para rodar a interface, descomente a linha "main()" no fim do arquivo.
# A interface usa menus e submenus, e cada menu chama a si mesmo depois
# de executar uma acao (em vez de usar while).
#
# Algumas opcoes estao marcadas como [nao implementado] - sao features
# que ficam para o aluno implementar depois.

def menu_principal():
    print()
    print("=== RESTAURANTE - MENU PRINCIPAL ===")
    print("1. Produtos")
    print("2. Pedidos")
    print("3. Calcular receita do dia")
    print("4. Sair")
    opcao = input("Opcao: ")

    if opcao == "1":
        menu_produtos()
    elif opcao == "2":
        menu_pedidos()
    elif opcao == "3":
        print("[receita do dia: ainda nao implementado]")  # TODO: chamar receita_do_dia() e mostrar o resultado
    elif opcao == "4":
        print("[sair: ainda nao implementado]")  # TODO: terminar o programa
    else:
        print("Opcao invalida")

    menu_principal()


def menu_produtos():
    print()
    print("--- PRODUTOS ---")
    print("1. Cadastrar produto")
    print("2. Alterar preco de produto")
    print("3. Voltar")
    opcao = input("Opcao: ")

    if opcao == "1":
        nome = input("  Nome do produto: ")
        preco = int(input("  Preco: "))
        cadastra(nome, preco)
        print(f"  Produto '{nome}' cadastrado com preco {preco}.")
        menu_produtos()
    elif opcao == "2":
        print("  [alterar preco: ainda nao implementado]")  # TODO: pedir nome e novo preco, chamar muda_preco(nome, novo_preco)
        menu_produtos()
    elif opcao == "3":
        return
    else:
        print("Opcao invalida")
        menu_produtos()


def menu_pedidos():
    print()
    print("--- PEDIDOS ---")
    print("1. Criar novo pedido")
    print("2. Adicionar produto a pedido")
    print("3. Remover produto de pedido")
    print("4. Voltar")
    opcao = input("Opcao: ")

    if opcao == "1":
        indice = cria_pedido()
        print(f"  Pedido criado com indice {indice}.")
        menu_pedidos()
    elif opcao == "2":
        indice = int(input("  Indice do pedido: "))
        produto = input("  Nome do produto: ")
        adiciona_ao_pedido(indice, produto)
        print(f"  Produto '{produto}' adicionado ao pedido {indice}.")
        menu_pedidos()
    elif opcao == "3":
        print("  [remover produto: ainda nao implementado]")  # TODO: pedir indice e nome do produto, chamar remove_do_pedido(indice, produto)
        menu_pedidos()
    elif opcao == "4":
        return
    else:
        print("Opcao invalida")
        menu_pedidos()


def main():
    menu_principal()


# Para rodar a interface CLI, descomente a linha abaixo:
# main()
