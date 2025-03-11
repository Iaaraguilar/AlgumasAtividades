def ler_inteiro():
    while True:
        try:
            valor = int(input("Digite um número inteiro: "))
            return valor
        except ValueError:
            print("Erro: Entrada inválida. Digite um número inteiro válido.")

numero = ler_inteiro()
print(f"Você digitou o número inteiro: {numero}")
