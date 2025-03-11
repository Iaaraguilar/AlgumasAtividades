nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2


match media:
 case media if media >= 7:
  print("Aluno aprovado.")
 case media if media >= 5:
  print("Aluno de exame.")
 case _:
  print("Aluno reprovado.")