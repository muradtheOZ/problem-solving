def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)- 1-i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr

print(bubble_sort([2,3,1,877,33,43334,89]))
