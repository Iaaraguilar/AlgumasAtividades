num=[-1, 2, -3, 4, -5, 6]
def lili(num):
    for i in range(len(num)):
        if num[i] < 0:
         num[i] = 0
    return num         
print(lili(num))