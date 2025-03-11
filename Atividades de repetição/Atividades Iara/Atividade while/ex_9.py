conta = 0

while True:
 num = int(input("Digite um número (-1 para sair): "))

 if num == -1:
   break
 
 if num % 2 == 0:
   conta += 1

print(f"Quantidade de números pares digitados: {conta}")