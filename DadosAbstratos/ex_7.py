#Uma central de atendimento telefônico gerencia chamadas em espera usando
# uma pilha. Isso significa que a última chamada recebida será a primeira a ser atendida.
# • Crie uma pilha vazia para armazenar as chamadas em espera.
# • Empilhe três chamadas com identificadores numéricos.
# • Mostre qual chamada será atendida primeiro.
# • Atenda a última chamada recebida e mostre a nova chamada no topo da pilha.
# • Verifique se ainda há chamadas na pilha após os atendimentos.




pilha_chamadas = []

pilha_chamadas.append(101)
pilha_chamadas.append(102)
pilha_chamadas.append(103)


if pilha_chamadas:
    print(f"A próxima chamada a ser atendida: {pilha_chamadas[-1]}")

if pilha_chamadas:
    print(f"Atendendo chamada: {pilha_chamadas.pop()}")

if pilha_chamadas:
    print(f"Nova chamada no topo: {pilha_chamadas[-1]}")
else:
    print("Nenhuma chamada restante na pilha.")


if pilha_chamadas:
    print("Ainda há chamadas na pilha.")
else:
    print("A pilha de chamadas está vazia.")
