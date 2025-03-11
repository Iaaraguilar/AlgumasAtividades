def multiplicar(a, b):
    try:
        return a * b
    except TypeError:
        print("Erro: Certifique-se de inserir apenas números.")
        return None


try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = multiplicar(num1, num2)
    if resultado is not None:
        print(f"O resultado da multiplicação é: {resultado}")
except ValueError:
    print("Erro: Entrada inválida. Digite apenas números.")
