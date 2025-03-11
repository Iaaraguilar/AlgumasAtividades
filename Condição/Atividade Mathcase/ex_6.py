senha = int(input("Escreva a senha: "))

match senha:
 case 1234:
  print("Acesso permitido")
 case _:
  print("Acesso negado")