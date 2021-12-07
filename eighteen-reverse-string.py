def reverse_string(s):
    n = len(s)
    m = n //2

    for i in range (m):
        s[i], s[n-1-i] = s[n-1-i],s[i]
    return s


print(reverse_string(["h","e","l","l","o"]))
