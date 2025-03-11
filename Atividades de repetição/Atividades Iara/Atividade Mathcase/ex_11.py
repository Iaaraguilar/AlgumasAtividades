salatual = float(input("Digite o salário atual do colaborador: R$ "))

if salatual <= 1500:
 aumento = 0.20
elif salatual <= 3000:
 aumento = 0.15
elif salatual <= 5000:
 aumento = 0.10
else:
 aumento = 0.05
 
aumento = salatual * aumento
novosalario = salatual + aumento
print(f"Salário atual: R$ {salatual:.2f}")
print(f"Aumento: R$ {aumento:.2f}")
print(f"Novo salário: R$ {novosalario:.2f}")