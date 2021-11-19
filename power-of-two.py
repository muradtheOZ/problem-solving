def isPowerOfTwo(n):
    i = 5
    if n<= 16 and (n == 1 or n == 2 or n== 4 or n==8 or n== 16):
        return True
    elif n > 16:
        while i <= n//4:
            if pow(2,i) == n:
                return True
            elif pow(2,i) > n:
                return False
            i += 1
        else:
            return False
result = isPowerOfTwo(1024)
print(result)