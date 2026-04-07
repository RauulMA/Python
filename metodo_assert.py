def podeVotar(nome: str, idade: int):
    assert idade > 0, "Digite um número positivo." #apenas verifica se há erros na produção, não na comercialização
    
    if idade < 16:
        return f"{nome} não tem direito ao voto."
    elif idade <= 18:
        return f"{nome} tem direito ao voto, mas seu voto não é obrigatório."
    elif idade < 70:
        return f"{nome} tem voto obrigatório."
    else:
        return f"{nome} tem direito ao voto, mas seu voto não é obrigatório."
        
def main():
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))

    status = podeVotar(nome, idade)
    
    print(f"\n{status}")
    
if __name__ == "__main__":
    main()