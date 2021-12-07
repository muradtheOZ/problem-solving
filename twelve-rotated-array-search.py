def search(nums, target):
    left,right = 0, len(nums) -1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[left] < nums[mid] and target < nums[mid] and target >= nums[left]:
            right = mid-1
        elif nums[mid] < nums[right] and target > nums[mid] and target <= nums[right]:
            left = mid + 1
        elif nums[left] > nums[mid]:
            right = mid -1
        else:
            left = mid + 1
    return -1
 
print(search([4,5,6,7,0,1,2,3],100))