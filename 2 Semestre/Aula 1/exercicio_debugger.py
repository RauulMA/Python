# =============================================================
# REVISAO - Lista 3: DEBUGGER (parte 1 de 2)
#
# Rode este arquivo com:   python3 exercicio_debugger.py
#
# Ele vai parar no primeiro exercicio que voce ainda nao fez.
# Resolva, rode de novo, e va seguindo.
#
# Esta lista eh diferente das duas anteriores. Aqui as funcoes ja vem
# ESCRITAS - e cada uma delas tem um bug plantado. O seu trabalho eh
# primeiro DESCOBRIR o que ela faz de errado (usando o debugger), e so
# depois consertar.
#
# Todo bug desta lista foi escolhido para ser dificil de ver LENDO e
# facil de ver PARANDO.
#
# As imagens citadas nas explicacoes estao na pasta `imagens/`, que vem
# junto com este arquivo.
# =============================================================

# === Helper de verificacao (pode ignorar) ===
# A funcao `verifica` compara o seu valor com a resposta correta (que
# fica escondida em formato de hash). Voce nao precisa entender ela -
# se voce errou, ela imprime "Valor errado: voce colocou X" e o assert
# logo abaixo dispara.
import hashlib
def verifica(valor, codigo, ordem_importa=False, nome_questao=''):
    if isinstance(valor, tuple):
        valor = list(valor)
    if isinstance(valor, dict):
        valor = sorted(valor.items())
    valores = [valor]
    if isinstance(valor, list):
        valores = [valor if ordem_importa else sorted(valor)]
    elif isinstance(valor, int) and not isinstance(valor, bool):
        valores.append(float(valor))
    elif isinstance(valor, float):
        valores.append(int(valor))
    def _hash(v):
        s = f'{nome_questao}:{v}' if nome_questao else str(v)
        return hashlib.sha224(s.encode('utf-8')).hexdigest()
    respostas = [_hash(v) == codigo for v in valores]
    if not any(respostas):
        print(f'Valor errado: voce colocou "{valor}" na variavel')
        return False
    return True


def explicar(questao):
    try:
        from explicacao_debugger import EXPLICACOES
    except ImportError:
        print("Arquivo 'explicacao_debugger.py' nao foi encontrado.")
        print("Esse arquivo vem JUNTO com este exercicio - peca ao")
        print("professor.")
        return
    import codecs
    if questao not in EXPLICACOES:
        print(f"Nao tenho explicacao para '{questao}'.")
        print(f"Questoes disponiveis: {sorted(EXPLICACOES.keys())}")
        return
    print(codecs.decode(EXPLICACOES[questao], 'rot_13'))
    input("aperte enter para continuar")
# fim do helper


# =============================================================
# ===== FUNCOES QUE JA ESTAO CERTAS =====
# =============================================================
#
# Estas duas voce ja escreveu nas Listas 1 e 2. Elas estao aqui
# PRONTAS e CORRETAS - o bug nunca esta nelas. Quando o debugger
# entrar numa delas, pode sair: nao ha nada pra achar la dentro.

def valor_da_carta(carta):
    valor = carta[0]
    if valor == 'A':
        return 1
    if valor == 'Q' or valor == 'J' or valor == 'K':
        return 10
    return int(valor)


def maximo2(a, b):
    if a > b:
        return a
    return b


# =============================================================
# ===== FASE 0 - Ligando o debugger =====
# =============================================================

'''
EXPLICACAO

Ate agora, quando um programa seu dava errado, voce tinha que reler o codigo ate achar, 
Ou usar o python tutor pra ver passo a passo

O python tutor é legal porque ele PARA o programa numa linha que voce
escolheu e deixa voce olhar, com calma, o valor de cada variavel naquele
exato momento. Nao eh o que voce acha que o programa faz: eh o que ele
esta fazendo.

Mas ele é limitado. Nessa aula, vamos usar o vscode como um 
'python tutor melhorado' e ver varias das vantagens

Sao cinco coisas pra ligar, na ordem. As imagens estao na pasta
`imagens/`, aqui do lado.

1) A EXTENSAO. No VSCode, instale a extensao "Python" (da Microsoft).
   Sem ela o menu do passo 3 nem aparece.

2) O BREAKPOINT. Eh o ponto onde o programa vai parar. Clique na margem
   esquerda, bem na esquerdinha do numero da linha: aparece uma bolinha
   vermelha.

   Veja `imagens/01_breakpoint_na_linha_de_dentro.png`. Repare BEM onde
   a bolinha esta: na primeira linha DE DENTRO da funcao, e nao na linha
   do `def`. A linha do `def` so diz "existe uma funcao chamada assim" -
   ela passa voando quando o arquivo carrega, e parar ali nao mostra
   nada. O que voce quer eh parar quando a funcao estiver RODANDO.

3) RODAR NO MODO DEBUG. Nao eh o play normal. Clique na setinha para
   baixo do lado do play e escolha "Python Debugger: Debug Python File".

   Veja `imagens/02_menu_do_play.png` - sao quatro opcoes, e voce quer a
   terceira.

4) A BARRA DE CONTROLES. Quando o programa para, aparece uma barrinha
   flutuante com os botoes de andar (`imagens/03_barra_de_controles.png`).
   Por enquanto guarde dois deles:

       step over  (`imagens/04_botao_step_over.png`) - anda UMA linha,
                  e se essa linha chama uma funcao, ele executa a funcao
                  inteira de uma vez e para na linha seguinte.

       step into  (`imagens/05_botao_step_into.png`) - anda UMA linha,
                  e se essa linha chama uma funcao, ele ENTRA nela e
                  para na primeira linha de dentro.

   A diferenca entre os dois eh o assunto da Fase 2.

5) ONDE OS VALORES APARECEM. Com o programa parado, os valores aparecem
   em dois lugares. Ao lado da propria linha, em cinza
   (`imagens/06_valores_inline.png` - repare no `lista = [2, 3, 4, 5]`
   escrito na frente da linha), e no painel da esquerda, que lista todas
   as variaveis vivas naquele momento.

   Tem ainda o painel WATCH (`imagens/07_painel_watch.png`), onde voce
   DIGITA uma expressao qualquer e ele te mostra quanto ela vale ali.
   Isso eh a Fase 3.

A seta amarela mostra a linha que vai ser executada AGORA - ou seja, ela
ainda NAO rodou. Esse detalhe importa mais do que parece, e a Fase 1 vive
dele.
'''

'''
EXERCICIO

Aquecimento, so pra garantir que voce achou o menu certo.

Voce clicou na setinha do lado do play e apareceram quatro opcoes
(`imagens/02_menu_do_play.png`). Qual delas roda o arquivo PARANDO nos
breakpoints?

    a) Run Python File
    b) Run Python File in Dedicated Terminal
    c) Python Debugger: Debug Python File
    d) Python Debugger: Debug using launch.json
'''
qual_opcao_do_play = 'c'   # 'a', 'b', 'c' ou 'd'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('qual_opcao_do_play')

assert verifica(qual_opcao_do_play, 'bfd2c66c9281cae7a4f4e2d11791a08cd082d2a659cc313572968f51', nome_questao='qual_opcao_do_play'), 'qual_opcao_do_play incorreta'

print('Exercicio fase 0 (ligando o debugger): OK')


# =============================================================
# ===== FASE 1 - Breakpoint e o painel de variaveis =====
# =============================================================

'''
EXPLICACAO

Primeira tecnica: parar numa linha e LER as variaveis.

A funcao abaixo eh a `cresce` da Lista 2 - a que acrescenta na mao uma
copia da ultima carta. So que esta versao esta bugada, e o bug eh do
tipo barulhento: ela ESTOURA. Rodar `cresce(['Ac', '5p'])` levanta um
erro.

Erro que estoura eh o comeco mais facil: o debugger te leva sozinho ate
a linha do crash, sem voce precisar escolher onde parar. O que ele NAO
te da de graca eh o porque - e eh isso que voce vai ler no painel.
'''

# ESTA FUNCAO ESTA BUGADA - voce vai consertar ela mais abaixo.
def cresce(mao):
    indice_ultima = len(mao)          # linha A
    ultima = mao[indice_ultima - 1]       # linha B
    mao.append(ultima)                # linha C
    return mao


def investiga_cresce():
    mao = ['Ac', '5p']
    return cresce(mao)


# COMO INVESTIGAR:
#   1. ponha um breakpoint na linha A (a primeira linha de dentro do
#      `def cresce`)
#   2. descomente a linha abaixo
#   3. rode com "Python Debugger: Debug Python File"
#   4. ande com step over e veja o que acontece na linha B
#
# investiga_cresce()

'''
EXERCICIO

Voce parou na linha A com a mao valendo ['Ac', '5p'].

De um step over (agora a linha A ja rodou) e olhe o painel de variaveis.

1) Quanto vale `indice_ultima`?
'''
valor_de_indice_ultima = 2

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('valor_de_indice_ultima')

assert verifica(valor_de_indice_ultima, 'ff69c6fe7a937e8d5b3650ea3eccbac628f50f59e762dac4d19d068f', nome_questao='valor_de_indice_ultima'), 'valor_de_indice_ultima incorreta'

'''
EXERCICIO

Ainda com a mao valendo ['Ac', '5p'] - que tem duas cartas, nas posicoes
0 e 1.

2) Qual eh o MAIOR indice que existe nessa mao?
'''
maior_indice_valido = 1

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('maior_indice_valido')

assert verifica(maior_indice_valido, '66421c62abca3363dfd9caaffe0b55409b9d409e28bac9e34c349099', nome_questao='maior_indice_valido'), 'maior_indice_valido incorreta'

'''
EXERCICIO

Compare as duas respostas acima. A linha B pede a carta na posicao
`indice_ultima` - uma posicao que a mao nao tem.

3) Que erro o Python levanta nessa hora? Responda com o NOME do erro,
   como texto: o debugger mostra ele em vermelho, e o terminal tambem.

   Formato da resposta: 'NomeDoErro' (com aspas, sem a mensagem que vem
   depois dos dois pontos).
'''
tipo_do_erro = 'IndexError'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('tipo_do_erro')

assert verifica(tipo_do_erro, 'd95f2d96cbd3a5b947eb362d536935113523c4486ffe953074dd7e52', nome_questao='tipo_do_erro'), 'tipo_do_erro incorreta'

'''
CONSERTO

Agora arrume a linha A da funcao `cresce`, la em cima.

O ultimo indice de uma lista nao eh `len(lista)` - eh um a menos. Essa eh
a mesma armadilha que a Q1 da Fase 2 da Lista 2 (`pegar_a_ultima`) ja
tinha nomeado; a diferenca eh que agora voce a viu acontecer.

Depois de consertar, os asserts abaixo passam.
'''

assert cresce(['Ac', '5p']) == ['Ac', '5p', '5p'], 'cresce deve repetir a ultima carta'
assert cresce(['Ko']) == ['Ko', 'Ko'], 'cresce com uma carta so'
assert cresce(['2c', '3c', '4c']) == ['2c', '3c', '4c', '4c'], 'cresce numa mao maior'

print('Exercicio fase 1 (breakpoint e painel de variaveis): OK')


# =============================================================
# ===== FASE 2 - Step OVER contra step INTO =====
# =============================================================

'''
EXPLICACAO

Segunda tecnica: escolher se voce ENTRA na funcao chamada ou nao.

O bug da Fase 1 era barulhento. Este eh o contrario: a `valor_da_mao`
abaixo roda inteira, sem erro nenhum, sem traceback nenhum - e devolve o
numero errado. Ninguem reclama. Esse eh o tipo de bug que chega no
usuario.

A `valor_da_mao` chama a `valor_da_carta` a cada volta do for. Entao,
parado na linha que faz a chamada, voce tem duas opcoes:

    step over  - executa a `valor_da_carta` inteira e para na linha
                 seguinte da `valor_da_mao`. Voce continua vendo a funcao
                 de FORA.
    step into  - entra na `valor_da_carta` e para na primeira linha dela.
                 Voce passa a ver a funcao de DENTRO.

Como saber qual usar? Depende de onde voce desconfia que o bug esta. A
`valor_da_carta` desta lista ja esta certa (ela esta la em cima, no bloco
das prontas), entao entrar nela eh perder tempo: aqui voce quer step
over, ficando na `valor_da_mao` e vendo o `total` mudar volta a volta.

Sabendo disso, o step into deixa de ser um botao misterioso e vira uma
decisao: eu confio nessa funcao ou nao?
'''

# ESTA FUNCAO ESTA BUGADA - voce vai consertar ela mais abaixo.
def valor_da_mao(mao):
    total = 0                                 # linha B
    for carta in mao:                             # linha A
        total = total + valor_da_carta(carta)     # linha C
    return total                                  # linha D


def investiga_valor_da_mao():
    mao = ['Ac', '5p', 'Ko', '3c']
    return valor_da_mao(mao)


# COMO INVESTIGAR:
#   1. ponha um breakpoint na linha C
#   2. descomente a linha abaixo e rode no modo debug
#   3. a cada vez que ele parar, olhe o `total` no painel ANTES e DEPOIS
#      de dar o step over
#   4. use "continue" (o play da barrinha) pra pular pra proxima volta
#
# investiga_valor_da_mao()

'''
EXERCICIO

Voce esta parado na linha C, que eh a linha
`total = total + valor_da_carta(carta)`.

Qual botao mostra as linhas de DENTRO da `valor_da_carta`?

    a) step over (`imagens/04_botao_step_over.png`)
    b) step into (`imagens/05_botao_step_into.png`)
    c) continue - o play da barrinha
    d) restart - a setinha circular
'''
over_ou_into = 'b'   # 'a', 'b', 'c' ou 'd'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('over_ou_into')

assert verifica(over_ou_into, '192d34307dd18bece138f9c4cf73c99a4bd8907cab0eb77634e93291', nome_questao='over_ou_into'), 'over_ou_into incorreta'

'''
EXERCICIO

Agora a observacao que interessa. A mao eh

    mao = ['Ac', '5p', 'Ko', '3c']

e os valores das cartas sao 1, 5, 10 e 3.

Percorra o for com o debugger e anote quanto vale o `total` DEPOIS da
linha C, em cada volta.

Nao responda de cabeca. A graca desta fase eh justamente que a resposta
que voce esperaria nao eh a que aparece no painel.

1) depois da 1a volta
'''
total_apos_1a_iteracao = 1

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('total_apos_1a_iteracao')

assert verifica(total_apos_1a_iteracao, '84e23c49a542f0504f3c9b3c6b68167fb0ebbbf615edacedff6461bc', nome_questao='total_apos_1a_iteracao'), 'total_apos_1a_iteracao incorreta'

'''
EXERCICIO

2) depois da 2a volta

   Cuidado com esta. Se voce somou 1 + 5 de cabeca, o painel vai discordar
   de voce - e quem esta certo eh o painel. Olhe a linha B antes de
   responder.
'''
total_apos_2a_iteracao = 5

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('total_apos_2a_iteracao')

assert verifica(total_apos_2a_iteracao, '4b85a4bad6fe10a839dc577267ff27b3a12e123d2b73c85fc1352fc6', nome_questao='total_apos_2a_iteracao'), 'total_apos_2a_iteracao incorreta'

'''
EXERCICIO

3) depois da 3a volta
'''
total_apos_3a_iteracao = 10

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('total_apos_3a_iteracao')

assert verifica(total_apos_3a_iteracao, '114fab6b1ff5052849b17f1efcce38cbab4325e1dcf577c4883230f2', nome_questao='total_apos_3a_iteracao'), 'total_apos_3a_iteracao incorreta'

'''
EXERCICIO

4) depois da 4a volta
'''
total_apos_4a_iteracao = 3

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('total_apos_4a_iteracao')

assert verifica(total_apos_4a_iteracao, '309fc6824ede0d93ce775b2af221855618ab2307c85cea852bab0334', nome_questao='total_apos_4a_iteracao'), 'total_apos_4a_iteracao incorreta'

'''
EXERCICIO

5) E, no fim, o que a linha D devolve?

   (A soma certa dessa mao seria 1 + 5 + 10 + 3 = 19. Nao eh isso que sai.)
'''
valor_retornado_por_valor_da_mao = 3

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('valor_retornado_por_valor_da_mao')

assert verifica(valor_retornado_por_valor_da_mao, 'a6b41592db81253ea48b38fa9ab24d3700c8296b73e88bc55ed69f22', nome_questao='valor_retornado_por_valor_da_mao'), 'valor_retornado_por_valor_da_mao incorreta'

'''
CONSERTO

Voce acabou de ver o `total` voltar pra zero a cada volta. Ele nao
acumula nada: no fim, ele guarda so o valor da ULTIMA carta.

Arrume a `valor_da_mao` movendo a linha B pra fora do for - o acumulador
precisa nascer ANTES do laco, senao ele renasce a cada volta.

Repare que esse bug eh de INDENTACAO: nenhuma palavra do codigo esta
errada, so o lugar de uma delas.
'''

assert valor_da_mao(['Ac', '5p', 'Ko', '3c']) == 19, 'a mao que voce percorreu no debugger vale 19'
assert valor_da_mao(['Ac', '5p', 'Qo']) == 16, 'outra mao qualquer'
assert valor_da_mao(['Qc']) == 10, 'mao de uma figura so'
assert valor_da_mao([]) == 0, 'mao vazia vale 0 - e repare que a versao bugada nem rodava neste caso'

print('Exercicio fase 2 (step over contra step into): OK')


# =============================================================
# ===== FASE 3 - O painel WATCH =====
# =============================================================

'''
EXPLICACAO

Terceira tecnica: o painel WATCH.

Ate agora voce so LEU variaveis que ja existiam. O WATCH deixa voce
PERGUNTAR: com o programa parado, voce digita uma expressao qualquer -
`len(lista)`, `sum(lista)`, `maximo2(a, b)` - e ele mostra quanto ela
vale ali naquele ponto.

Veja `imagens/07_painel_watch.png`: o `+` no topo do painel adiciona uma
expressao nova. A ultima linha da imagem mostra o que acontece quando
voce pergunta por algo que nao existe naquele escopo - ele responde
`NameError`, em vez de inventar um valor.

Isso serve pra uma coisa que print nenhum faz bem: comparar o que a
funcao DEVOLVE com o que ela DEVERIA devolver, no mesmo instante e com
os mesmos argumentos.

A `maximo3` abaixo tem um bug traicoeiro: ela acerta em varios casos.
'''

# ESTA FUNCAO ESTA BUGADA - voce vai consertar ela mais abaixo.
def maximo3(a, b, c):
    maior = maximo2(maximo2(a, b), c)     # linha A
    return maior              # linha B


def investiga_maximo3():
    print(maximo3(1, 20, 3))
    print(maximo3(1, 2, 30))


# COMO INVESTIGAR:
#   1. ponha um breakpoint na linha B
#   2. descomente a linha abaixo e rode no modo debug
#   3. parado ali, adicione no WATCH a expressao:  maximo2(maximo2(a, b), c)
#   4. compare o valor dela com o `maior` que a funcao vai devolver
#
# investiga_maximo3()

'''
EXERCICIO

1) Quanto a funcao devolve em `maximo3(1, 20, 3)`?

   (Este caso passa. E eh justamente por isso que ele eh perigoso.)
'''
resultado_de_maximo3_1_20_3 = 20

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('resultado_de_maximo3_1_20_3')

assert verifica(resultado_de_maximo3_1_20_3, '3e8a01b1246c95e08aecc019cd720da99a3ffb110ef983879032b742', nome_questao='resultado_de_maximo3_1_20_3'), 'resultado_de_maximo3_1_20_3 incorreta'

'''
EXERCICIO

2) E em `maximo3(1, 2, 30)`?

   Agora o maior dos tres esta na TERCEIRA posicao. Olhe o `maior` no
   painel, na linha B, antes de responder.
'''
resultado_de_maximo3_1_2_30 = 2

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('resultado_de_maximo3_1_2_30')

assert verifica(resultado_de_maximo3_1_2_30, 'a3e1537e612bba6af091725173b9d21b8dfad7d8ca02ac24e201f283', nome_questao='resultado_de_maximo3_1_2_30'), 'resultado_de_maximo3_1_2_30 incorreta'

'''
EXERCICIO

3) Agora o WATCH. Parado na linha B durante a chamada
   `maximo3(1, 2, 30)`, digite no painel WATCH:

       maximo2(maximo2(a, b), c)

   Quanto ela vale?

   Repare no contraste: essa expressao e a funcao estao no mesmo ponto do
   programa, com os mesmos a, b e c - e dao respostas diferentes.
'''
watch_maximo2_de_maximo2 = 30

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('watch_maximo2_de_maximo2')

assert verifica(watch_maximo2_de_maximo2, '0207c0210b96d2b16da9270171a450de0b367e4adcbc438409c94a72', nome_questao='watch_maximo2_de_maximo2'), 'watch_maximo2_de_maximo2 incorreta'

'''
EXPLICACAO

Guarde o que acabou de acontecer: **um teste que passa nao prova que a
funcao esta certa.**

A `maximo3(1, 20, 3)` devolveu 20, que eh a resposta correta. Se o seu
unico teste fosse esse, voce teria dado a funcao por boa - e ela ignora o
terceiro argumento inteiro.

Eh por isso que as listas insistem em asserts de caso limite: colocar o
maior em CADA uma das tres posicoes. Um caso so nao distingue "funciona"
de "funciona por acidente". Na Lista 1, os asserts da familia `maximo`
faziam exatamente isso, e agora voce viu o que eles pegam.
'''

'''
CONSERTO

Arrume a `maximo3` la em cima. O `maior` da linha A so olhou `a` e `b` -
falta comparar o resultado com `c` antes do return.

Uma linha nova resolve.
'''

assert maximo3(30, 1, 2) == 30, 'o maior na PRIMEIRA posicao'
assert maximo3(1, 30, 2) == 30, 'o maior na SEGUNDA posicao'
assert maximo3(1, 2, 30) == 30, 'o maior na TERCEIRA posicao - o caso que a versao bugada errava'
assert maximo3(1, 20, 3) == 20, 'o caso que passava mesmo com o bug'
assert maximo3(5, 5, 5) == 5, 'todos iguais'
assert maximo3(-1, -2, -3) == -1, 'negativos'

print('Exercicio fase 3 (o painel WATCH): OK')


# =============================================================
# ===== FASE 4 - Simulacao integrada =====
# =============================================================

'''
EXPLICACAO

Fecho da parte 1. As duas funcoes de baralho que voce consertou -
`cresce` e `valor_da_mao` - rodam agora em sequencia, sobre a mesma mao.

Lembre da Lista 2: `cresce` MUTA a mao que recebeu. Depois dela, a mao
nao eh mais a mesma - e a previsao seguinte tem que levar isso em conta.

Responda cada previsao ANTES de olhar o resultado.
'''

mao_simulacao = ['Ac', '5p', 'Qo']

'''
EXERCICIO

1) Quanto vale a mao ['Ac', '5p', 'Qo']?
'''
valor_da_mao_inicial = valor_da_mao(['Ac', '5p', 'Qo'])

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('valor_da_mao_inicial')

assert verifica(valor_da_mao_inicial, 'f46008ea3c66fa6e767b334e2b7b918111c868905014d135f122cf90', nome_questao='valor_da_mao_inicial'), 'valor_da_mao_inicial incorreta'
assert valor_da_mao(mao_simulacao) == valor_da_mao_inicial, 'a sua previsao tem que bater com a funcao'

'''
EXERCICIO

2) Agora roda `cresce(mao_simulacao)`. Como fica a mao?

   Responda com a lista inteira, na ordem.
'''
mao_depois_do_cresce = ['Ac', '5p', 'Qo', 'Qo']

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('mao_depois_do_cresce')

assert verifica(mao_depois_do_cresce, '584b45c5f0ea729e024c799b04d16d183ffa37b78fa3030bd07cb223', ordem_importa=True, nome_questao='mao_depois_do_cresce'), 'mao_depois_do_cresce incorreta'

cresce(mao_simulacao)
assert mao_simulacao == mao_depois_do_cresce, 'a sua previsao tem que bater com a funcao'

'''
EXERCICIO

3) E quanto a mao passa a valer, agora que ela cresceu?
'''
valor_depois_do_cresce = valor_da_mao(['Ac', '5p', 'Qo', 'Qo'])

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('valor_depois_do_cresce')

assert verifica(valor_depois_do_cresce, 'abce19896ecc3f6f3331b7953e979fc73eb5a4c2e3f30e901430b38a', nome_questao='valor_depois_do_cresce'), 'valor_depois_do_cresce incorreta'
assert valor_da_mao(mao_simulacao) == valor_depois_do_cresce, 'a sua previsao tem que bater com a funcao'

print('Exercicio fase 4 (simulacao integrada): OK')


print('\n=== PARABENS! Parte 1 completa! ===')
print('A parte 2 esta em ../03_debugger2/exercicio_debugger2.py')
print('La voce escolhe ONDE parar (em vez de apertar step 40 vezes) e')
print('ve o estado de uma lista mudando debaixo do nariz.')
