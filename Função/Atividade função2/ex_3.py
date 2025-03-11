num=[3,2,4,12,1,10,6]
def lili(num):
 cont=0
 for i in num:
    if i % 3==0: 
      cont+=1
 return cont  

print(lili(num))            