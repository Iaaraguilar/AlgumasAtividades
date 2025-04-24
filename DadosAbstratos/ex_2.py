#Criar uma pilha e manipular seus elementos.
#1. Crie uma pilha utilizando uma lista.
#2. Empilhe 3 números inteiros de sua escolha.
#3. Mostre o topo da pilha.
#4. Desempilhe o topo e mostre o novo topo.
#5. Tente desempilhar todos os elementos e mostrar se a pilha ficou vazia.



pilha=[]

pilha.append(1)
pilha.append(2)
pilha.append(3)

print("Topo da pilha: ",pilha[-1])

print("item removido: ",pilha.pop())
print("Topo da pilha: ",pilha[-1])
print("item removido: ",pilha.pop())
print("Topo da pilha: ",pilha[-1])
print("item removido: ",pilha.pop())
print("A lista esta vazia?: ",len(pilha) ==0)