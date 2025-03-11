produto1 = float(input("Digite o preço do primeiro produto: R$ "))
produto2 = float(input("Digite o preço do segundo produto: R$ "))
produto3 = float(input("Digite o preço do terceiro produto: R$ "))
if produto1 < produto2 and produto1 < produto3:
    print("Você deve comprar o primeiro produto, que custa R$", produto1)
elif produto2 < produto1 and produto2 < produto3:
    print("Você deve comprar o segundo produto, que custa R$", produto2)
else:
    print("Você deve comprar o terceiro produto, que custa R$", produto3)
