letra = input('Digite uma palavra: ')
vogais = ['a', 'e', 'i', 'o', 'u']

def contaVogais(letra):
    contador = 0
    for i in letra:
        if i in vogais:
            contador += 1
    return contador

print(contaVogais(letra))