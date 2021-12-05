def hotel(arrive, depart, K):
    arrive.sort()
    depart.sort()

    count = 0
    n = len(arrive)

    i , j = 0, 0
    while i< n and j < n:
        if arrive[i] < depart[j]:
            count+= 1
            if count > K:
                return False
            i+= 1
        else:
            count -= 1
            j+= 1
    return True

A = [1,3,5,5,5,5,5,5,5,5,5,5]
B = [2,6,8,9,10,12,15,16,10,11,12,16]
c = 10

print(hotel(A,B,c))
