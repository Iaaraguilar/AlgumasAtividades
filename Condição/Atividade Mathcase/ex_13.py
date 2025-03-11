opcao = input("Você quer converter de Fahrenheit para Celsius ou de Celsius para Fahrenheit? ").upper()
if opcao == "F":
    fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5 / 9
    print(f"{fahrenheit}°F é igual a {celsius:.2f}°C.")
elif opcao == "C":
    celsius = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"{celsius}°C é igual a {fahrenheit:.2f}°F.")
else:
    print("Opção inválida! Digite 'F' para Fahrenheit para Celsius ou 'C' para Celsius para Fahrenheit.")
