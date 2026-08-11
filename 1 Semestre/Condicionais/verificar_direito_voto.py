def verificar_idade_positiva(mensagem):
    while True:
        try:
            valor  = float(input(mensagem))
            if valor < 0:
                print("Insira um valor positivo.")
                continue
            return valor
        except ValueError:
            print("Insira um valor numérico.")

def identificar_qualidades(idade):
    voto_opcional = (16 <= idade < 18) or (idade >= 70)
    voto_obrigatorio = 18 <= idade < 70
    direito_ao_voto = idade >= 16
    Texto_definitivo = print(f"Segue suas qualidades referentes a sua idade: \nVoto opcional: {voto_opcional}\nVoto Obrigatório: {voto_obrigatorio}\nDireito ao voto: {direito_ao_voto}")
    return Texto_definitivo

def main():
    idade = verificar_idade_positiva("Digite sua idade: ")
    identificar_qualidades(idade)

if __name__ == "__main__":
    main()