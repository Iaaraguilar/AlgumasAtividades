num=int(input("Digite um numero: "))
def tabu(num):
   for x in (1, 2, 3, 4, 5, 6 , 7, 8, 9, 10):
    print(f"{num} x {x} = {num * x}")
print(tabu(num))    
