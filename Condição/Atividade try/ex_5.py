def soma_lista(numeros):
    try:
        return sum(int(num) for num in numeros)
    except ValueError:
        print("Erro: A lista contém valores inválidos. Certifique-se de inserir apenas números.")
        return None


entrada = input("Digite os números separados por espaço: ")
numeros = entrada.split()

resultado = soma_lista(numeros)
if resultado is not None:
    print("A soma dos números é:", resultado)
