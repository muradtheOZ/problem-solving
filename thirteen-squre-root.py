def my_sqrt(x):
    if x == 0:
        return 0
    def search_sqrt(left,right):
        if left > right:
            return right
        if left == right:
            return left
        mid = (left + right) // 2
        sqrt = mid*mid
        if sqrt == x:
            return mid
        if sqrt > x:
            return search_sqrt(left, mid-1)
        if sqrt < x:
            return search_sqrt(mid + 1, right)
    root = search_sqrt(1,x)

    if root * root > x:
        return root -1
    return root 



print(my_sqrt(5))