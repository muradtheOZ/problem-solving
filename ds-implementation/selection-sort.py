def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_value = i
        for j in range(i+1,n):
            if arr[j] < arr[min_value]:
                min_value = j

        if min_value != i:
            temp = arr[i]
            arr[i] = arr[min_value]
            arr[min_value] = temp
    return arr

unsorted_array = [3,4,676,987,5,13,1,123,15]
sorted_array = selection_sort(unsorted_array)

print(sorted_array)