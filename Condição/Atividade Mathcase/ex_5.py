num1 = int(input("Digite o primeiro número: "))
num2= int(input("Digite o segundo número: "))

match num1== num2:
 case True:
  print("Eles são iguais")
 case _:
  print("Eles são diferentes")