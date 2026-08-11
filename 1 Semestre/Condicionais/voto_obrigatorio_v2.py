def pode_votar(nome: str, idade: int) -> str:
    assert idade > 0, "Digite um número positivo."
    if idade < 16:
        return f"{nome} não tem direito ao voto."
    elif (idade < 18) or (idade >= 70):
        return f"{nome} tem direito ao voto, mas seu voto não é obrigatório."
    else:
        return f"{nome} tem voto obrigatório."
    
def verificar_idade_positiva(mensagem: str) -> int:
    while True:
        try:
            valor = int(input(mensagem))
            if valor <= 0:
                print("Digite um valor maior que zero.")
                continue
            return valor
        except ValueError:
            print("Digite um valor numérico.")

def verificar_nome_vazio(mensagem: str) -> str:
    while True:
        valor = input(mensagem).strip()
        if not valor:
            print("Digite algum nome.")
            continue
        return valor

        
def main():
    nome = verificar_nome_vazio("Digite seu nome: ")
    idade = verificar_idade_positiva("Digite sua idade: ")

    status = pode_votar(nome, idade)
    
    print(f"\n{status}")
    
if __name__ == "__main__":
    main()