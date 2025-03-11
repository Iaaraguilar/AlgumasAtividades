valor = float(input("Escreva um valor: "))
match valor:
 case valor if valor > 0:
  print("Esse número é positivo: ")
 case valor if valor < 0:
  print("Esse número é negativo: ")
 case _:
  print("Esse número é neutro: ")