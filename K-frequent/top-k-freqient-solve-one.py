def frequent_k_element(list,k):
    list.sort()
    new_list = []
    result = []
    count = 1
    for i in range (len(list)):
        if i < len(list)-1 and list[i] == list[i +1]:
            count += 1
            continue
        new_list.append((count,list[i]))
        count = 1
    new_list.sort(reverse=True)
    #print (new_list)
    for i in range(k +1):
        result.append(new_list[i][1])
    return result

nums = [1,2,5,9,9,9,9,9,3,4,4,5,5,5,5,5,9,9,9]
print(frequent_k_element(nums,2))



