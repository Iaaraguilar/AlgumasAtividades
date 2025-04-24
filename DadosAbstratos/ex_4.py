#Criar uma implementação simples de uma fila (Queue) usando listas. 
# 1. Crie uma fila vazia.
# 2. Enfileire 3 números inteiros na fila.
# 3. Mostre o primeiro elemento da fila. 
# 4. Desenfileire o primeiro elemento e mostre o novo primeiro elemento. 
# 5. Verifique se a fila está vazia após as remoções.

from collections import deque

fila= deque()

fila.append(2)
fila.append(4)
fila.append(6)

print("Topo da fila: ",fila[0])
print("item removido: ",fila.popleft())
print("Topo da fila: ",fila[0])
print("A fila esta vazia?: ",len(fila)==0)