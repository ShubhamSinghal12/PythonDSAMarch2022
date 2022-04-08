

arr = [1,-20,3,4,5]

def printSubArrays(arr):

    for i in range(len(arr)):
        for j in range(i,len(arr)):
            for k in range(i,j+1):
                print(arr[k],end = " ")
            print()

def SumOfSubArrays(arr):
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            sum = 0
            for k in range(i,j+1):
                sum += arr[k]
            print((i,j),sum)

def SumOfSubArrays2(arr):
    for i in range(len(arr)):
        sum = 0
        for j in range(i,len(arr)):
            sum += arr[j]
            print((i,j),sum)

def MaxSumOfSubArrays2(arr):
    max = arr[0]
    for i in range(len(arr)):
        sum = 0
        for j in range(i,len(arr)):
            sum += arr[j]
            print((i,j),sum)
            if sum > max:
                max = sum
    
    print("max = ",max)

def kadanes(arr):
    
    max = arr[0]
    sum = 0 
    for i in range(len(arr)):
        sum += arr[i]

        print(i,sum)

        if sum > max:
            max = sum
        
        if sum < 0:
            sum = 0
    
    print("Max = ",max)

MaxSumOfSubArrays2(arr)
kadanes(arr)