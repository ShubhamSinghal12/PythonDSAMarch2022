n = 28

flag = 0
i = 2
while i <= n-1:
    
    if n%i == 0:
        flag += 1
        # print(i,end=" ")
        break
    
    i += 1

if flag == 0:
    print("Prime")
else:
    print("Not Prime")