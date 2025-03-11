def fatorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

numero = int(input("Digite um número: "))
resultado = fatorial(numero)
print("O fatorial de", numero, "é", resultado)