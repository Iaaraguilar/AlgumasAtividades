def pegar_elemento(lista, indice):
    try:
        return lista[indice]
    except IndexError:
        return "Erro: Índice fora do alcance da lista."
    except TypeError:
        return "Erro: O índice deve ser um número inteiro."


numeros = input("Digite os números da lista separados por espaço: ")
lista = [int(num) for num in numeros.split()]


try:
    indice = int(input("Digite o índice do elemento que deseja acessar: "))
    print("Elemento encontrado:", pegar_elemento(lista, indice))
except ValueError:
    print("Erro: O índice deve ser um número inteiro.")