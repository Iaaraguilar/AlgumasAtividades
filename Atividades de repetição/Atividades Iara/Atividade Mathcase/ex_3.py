idade = int(input("Digite sua idade: "))

match idade:
 case idade if idade >= 18:
  print("Você é de maior")
 case _:
  print("Você é de menor")