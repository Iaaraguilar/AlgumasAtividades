def ler_inteiro(numeros):
    try:
        if not numeros:
            raise ValueError("Erro: A lista de números está vazia. Não é possível calcular a média.")
        return sum(numeros) / len(numeros)
    except ValueError as e:
        return str(e)

numeros_teste = [10, 20, 30, 40]
print(f"A média dos números é: {ler_inteiro(numeros_teste)}")
print(ler_inteiro([]))
