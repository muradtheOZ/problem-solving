def remove_Duplicates(nums):
    n = len(nums)
    index = 1
    for i in range( 1,n):
        if nums[i] != nums[i-1]:
            nums[index]= nums[i]
            index += 1
    return index

array = [1,2,3,9,9,9,10,10,20,20,20,20,20,21,21]
print(remove_Duplicates(array))