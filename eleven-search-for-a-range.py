def search_range(nums, target): 
    start_index = -1
    end_index = -1
    result = [] 
    i = 0
    for i in range (len(nums)):
        if target == nums[i]:
            if start_index < 0:
                start_index = i
            if target == nums[i]:
                end_index = i
                    
    result.append(start_index)
    result.append(end_index)
    return result
    
print(search_range([1,2,3,4,4,4,5,6,7,7,7,8], 7))