turno = input("Em que turno você estuda? (M - Matutino, V - Vespertino, N - Noturno): ").upper()
match turno:
 case "M":
  print("Bom Dia!")
 case "V":
  print("Boa Tarde!")
 case "N":
  print("Boa Noite!")
 case _:
  print("Valor Inválido!")