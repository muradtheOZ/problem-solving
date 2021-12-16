def binary_search(arr,val):
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = (left + right)// 2
        if(arr[mid] == val):
            return 1
        if arr[mid] > val:
            right = mid -1
        else:
            left = mid + 1
    return -1

box = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,122222222222222222,1233333333333333333333345]
number = 14
print(binary_search(box,number))
    