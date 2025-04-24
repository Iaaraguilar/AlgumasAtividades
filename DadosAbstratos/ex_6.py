#Uma impressora trabalha com um sistema de fila para processar documentos
# enviados para impressão. Cada documento enviado entra no final da fila e será
# impresso na ordem em que chegou.
# • Crie uma fila vazia para representar a fila de impressão.
# • Enfileire três documentos (nomes de arquivos) na fila.
# • Mostre qual documento será impresso primeiro.
# • Desenfileire o primeiro documento e mostre o próximo da fila.
# • Verifique se ainda há documentos na fila após as remoções.


fila_impressao = []


fila_impressao.append("documento1.pdf")
fila_impressao.append("documento2.pdf")
fila_impressao.append("documento3.pdf")


if fila_impressao:
    print(f"O primeiro documento a ser impresso: {fila_impressao[0]}")


if fila_impressao:
    print(f"Imprimindo: {fila_impressao.pop(0)}")


if fila_impressao:
    print(f"Próximo documento na fila: {fila_impressao[0]}")
else:
    print("Nenhum documento restante na fila.")
if fila_impressao:
    print("Ainda há documentos na fila.")
else:
    print("A fila de impressão está vazia.")