r = [0,2,1,3,0,1,2,1,2,1]
n = 10

def RainWaterHarvesting(arr, n):

    larr = [0 for i in range(n)]
    rarr = [0 for i in range(n)]
    water = 0
    larr[0] = arr[0]
    for i in range( 1, n):
        larr[i] = max(larr[i-1], arr[i])

    rarr[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        rarr[i] = max(rarr[i + 1], arr[i])

    for i in range(0, n):
        water += min(larr[i], rarr[i]) - arr[i]

    print(water)


RainWaterHarvesting(r, n)
