def max_sub_array(nums):
    if len(nums) == 0:
            return 0
    if len(nums) == 1:
            return nums[0]
        
    max = -100000
    current_result = 0
    for i in range(len(nums)):
        current_result += nums[i]
        if current_result > max:
                max = current_result
        if current_result < 0:
            current_result = 0
    return max

array = [-1000,-100,-10,-1]
print(max_sub_array(array))
    
            
        