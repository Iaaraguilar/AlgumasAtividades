idade = int(input("Digite sua idade: "))
match idade:
 case idade if idade <= 11:
  print("Criança")
 case idade if idade <= 18:
  print("Adolescente")
 case idade if idade <= 24:
  print("Jovem")
 case idade if idade <= 40:
  print("Adulto")
 case idade if idade <= 60:
  print("Meia Idade")
 case _:
  print("Idoso")