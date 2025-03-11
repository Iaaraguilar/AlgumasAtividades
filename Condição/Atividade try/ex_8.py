def contar_caracteres(texto, caractere):
    try:

        if not isinstance(texto, str):
            raise ValueError("O texto precisa ser uma string.")
        
     
        contagem = texto.count(caractere)
        return contagem

    except ValueError as e:
        return f"Erro: {e}"


texto = input("Digite o texto: ")
caractere = input("Digite o caractere que deseja contar: ")


resultado = contar_caracteres(texto, caractere)
print(resultado)
