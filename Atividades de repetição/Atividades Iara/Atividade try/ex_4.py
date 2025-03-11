
a = int(input("Digite um número inteiro: "))
b = int(input("Digite um número inteiro: "))    

def divisao_segura(a, b):
    try:
        return a / b  
    except ZeroDivisionError: 
        return "Erro: Divisão por zero não permitida!"  

print(divisao_segura(a, b))
