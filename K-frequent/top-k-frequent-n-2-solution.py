def frequent_k_element(nums,k):
    new_list = []
    count = 1
    i = 0
    poper = 0
    result = []
    previous_length = len(nums)
    
    popper_counter = 0

    if len(nums) == k:
        return nums

    while i < len(nums):
        for j in range(len(nums)-1):
            if  nums[i] == nums[j+1]:
                count += 1
        new_list.append((count,nums[i]))
        found_number = nums[i]

        count = 1
        
        while poper < len(nums):
            if found_number == nums[poper]:
                nums.pop(poper)
            else:
                poper += 1
          
        poper = 0
        
    new_list.sort(reverse=True)
    for i in range(k):
        result.append(new_list[i][1])
    return result

nums = [3,0,1,0]

print(frequent_k_element(nums,1))



