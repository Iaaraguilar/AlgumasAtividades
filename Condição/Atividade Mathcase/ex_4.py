temp = float(input("Digite a temperatura: "))

match temp:
 case temp if temp >= 30:
  print("Está quente")
 case temp if temp <=15:
  print("Está frio")
 case _:
  print("Está agradável")