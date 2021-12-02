def sub_unsort(A):
    sorted_arrya = sorted(A)
    counter = []
    empty = []
    for i in range(len(sorted_arrya)-1):
        if sorted_arrya[i] != A[i]:
            counter.append(i)
            break
    for i in range (len(sorted_arrya)-1,0,-1):
        if sorted_arrya[i] != A[i]:
            counter.append(i)
            break
    if counter != empty :
        return counter
    else:
        return [-1]

print(sub_unsort([1,2,7,9,42,3,4,6,8,9100]))