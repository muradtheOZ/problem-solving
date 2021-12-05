from collections import Counter
def frequent_k_element(nums,k):
    result = []
    count = Counter(nums)
    
    tuple_set = count.most_common()
    for i in range(k):
        result.append(tuple_set[i][0])
    
    return result


nums = [1,2,5,9,9,9,9,9,3,4,4,5,5,5,5,5,9,9,9]
print(frequent_k_element(nums,2))



