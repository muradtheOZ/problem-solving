def maximum_gap(A):
    numbers = []
    for i,num in enumerate(A):
        numbers.append((num,i))
    numbers.sort()
    max_gap = 0
    min_index = numbers[0][1]

    for item in numbers:
        index = item[1]
        if index <= min_index:
                min_index = index
        else:
            max_gap = max(max_gap, index - min_index)
    return max_gap
array = [10,1,40,3,323,2,323,323,34,6,65,7,-9,-12,-10]
print(maximum_gap(array))

