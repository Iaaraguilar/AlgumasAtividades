num1=float(input("Digite o primeiro número: "))
num2=float(input("Digite o segundo número: "))
soma = num1 + num2

match soma:
 case soma if soma > 15:
  print("Seu resultado é:")
 case _:
  print("Seu resultado é menor que 15")