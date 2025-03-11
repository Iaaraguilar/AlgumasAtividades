n = int(input("Digite o número para calcular o fatorial: "))
num = 1 
for i in range(1, n + 1):  
    num *= i  
print(f"O fatorial de {n} é {num}")
