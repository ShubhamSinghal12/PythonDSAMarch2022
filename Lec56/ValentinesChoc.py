def vc(boys,girls,i,j):
    if i == len(boys):
        return 0
    elif j == len(girls):
        return 10**8
    else:
        return min(abs(boys[i]-girls[j])+vc(boys,girls,i+1,j+1),vc(boys,girls,i,j+1))


boys = [4,5]
girls = [1,2,3,4,5]

print(vc(boys,girls,0,0))