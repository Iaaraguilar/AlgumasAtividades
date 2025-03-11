time1 = int(input("Digite os gols do primeiro time: "))
time2 = int(input("Digite os gols do segundo time: "))


match time1 - time2:
 case 0:
  print("O jogo terminou em empate.")
 case gols if time1 > time2:
  print("O primeiro time venceu.")
 case _:
  print("O segundo time venceu.")