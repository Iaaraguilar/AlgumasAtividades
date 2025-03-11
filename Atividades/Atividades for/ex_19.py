palavra = input("Digite uma palavra: ").lower()  
letra = input("Digite uma letra: ").lower()  
contador = 0  
for char in palavra:
    if char == letra:  
        contador += 1  
print(f"A letra '{letra}' aparece {contador} vez(es) na palavra '{palavra}'.")
