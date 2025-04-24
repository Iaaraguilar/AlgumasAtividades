#pilha
#pilha= []
#adicionar
#pilha.append(10)
#pilha.append(6)
#pilha.append(25)
#ver o topo
#print("topo da pilha: ",pilha[-1])
#remover
#print("removido: ", pilha.pop())
#print(pilha)
#print("A pilha esta vazia? ",len(pilha) == 0 )




#Fila
#importanto
from collections import deque

fila= deque()
#enfileirar
fila.append(10)
fila.append(8)
fila.append(55)


#mostrar primeiro elementoasaws



print("Removido: ", fila.popleft())
print("Primeiro da fila: ",fila[0])
print("A fila esta vazia? ",len(fila) == 0 )