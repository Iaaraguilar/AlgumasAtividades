maior = 0

while True:
 num = int(input("Digite um número (0 para sair): "))

 if num == 0:
  break

 if num > maior:
  maior = num
print("O maior número digitado foi:", maior)