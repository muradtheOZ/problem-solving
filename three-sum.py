def threeSum(nums):
    if len(nums) < 3:
        return []
    nums.sort()

    result = []

    n = len(nums)
    
    i = 0
    while i < n -2:
        k = n-1
        j = i +1
        while j < k:
            s = nums[i] + nums[j] + nums [k]
            if s == 0:
                result.append([nums[i], nums[j], nums [k]])
                while nums[j] == nums[j+1] and j < k-1:
                    j += 1
                while nums[k] == nums[k-1] and j < k-1:
                    k -= 1
                j += 1
            elif s > 0:
                k -= 1
            else:
                j += 1
        while i < n-3 and nums[i] == nums[i +1]:
            i += 1
        i += 1
    return result

nums = [-1,0,1,2,-1,-4]
result = threeSum(nums)
print(result)
