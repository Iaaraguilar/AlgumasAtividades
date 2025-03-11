
n = int(input("Digite um número para gerar o triângulo numérico: "))
for i in range(1, n + 1):
  
    print(' '.join(str(x) for x in range(1, i + 1)))
