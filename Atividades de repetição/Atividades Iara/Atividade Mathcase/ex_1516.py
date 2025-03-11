
pergunta1 = input("Telefonou para a vítima? (sim/não): ").strip().lower()
pergunta2 = input("Esteve no local do crime? (sim/não): ").strip().lower()
pergunta3 = input("Mora perto da vítima? (sim/não): ").strip().lower()
pergunta4 = input("Devia para a vítima? (sim/não): ").strip().lower()
pergunta5 = input("Já trabalhou com a vítima? (sim/não): ").strip().lower()
simrespostas = sum([pergunta1 == "sim", pergunta2 == "sim", pergunta3 == "sim", pergunta4 == "sim", pergunta5 == "sim"])
if simrespostas == 2:
    print("Classificação: Suspeita")
elif simrespostas >= 3 and simrespostas < 5:
    print("Classificação: Cúmplice")
elif simrespostas == 5:
    print("Classificação: Assassino")
else:
    print("Classificação: Inocente")
