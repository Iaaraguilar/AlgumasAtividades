#Você foi contratado para desenvolver uma funcionalidade de “Desfazer/Refazer" para um editor de texto simples. 
# O editor permite que o usuário escreva palavras em um documento, e, caso cometa um erro, pode desfazer a última ação ou refazê-la caso mude de ideia.

documento = []
refazer = []

while True:
    print("\nDocumento:")
    for palavra in documento:
        print(palavra)
    if not documento:
        print("Vazio")
    
    opcao = input("[1] Adicionar | [2] Desfazer | [3] Refazer | [4] Sair: ")
    
    if opcao == "1":
        documento.append(input("Digite a palavra: "))
    elif opcao == "2" and documento:
        refazer.append(documento.pop())
    elif opcao == "3" and refazer:
        documento.append(refazer.pop())
    elif opcao == "4":
        break 
     


    



