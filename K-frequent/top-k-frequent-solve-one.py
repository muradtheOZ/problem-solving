def frequent_k_element(nums,k):
    nums.sort()
    new_list = []
    result = []
    count = 1
    for i in range (len(nums)):
        if i < len(nums)-1 and nums[i] == nums[i +1]:
            count += 1
            continue
        new_list.append((count,nums[i]))
        count = 1
    new_list.sort(reverse=True)
    #print (new_list)
    for i in range(k):
        result.append(new_list[i][1])
    return result

nums = [1,2]
print(frequent_k_element(nums,2))



