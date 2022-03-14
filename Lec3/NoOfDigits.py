import math
num = int(input())
nod = 0
num2 = num
while num != 0:
    num = num//10
    nod += 1

print(nod)

print(int(math.log10(num2))+1)