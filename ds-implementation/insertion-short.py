def insertion_short(arr):
    n = len(arr)
    item = None
    for i in range (1,n):
        item = arr[i]
        j = i -1
        while(j >=0 and arr[j]>item):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j+1] = item
    return arr

print(insertion_short([5,4,3,2,1,100,500,400]))
