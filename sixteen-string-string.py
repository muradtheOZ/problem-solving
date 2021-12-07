def str_str(haystack, needle):
    if haystack == []:
        return 0
    n = len(haystack)
    m = len(needle)
    i = 0
    while i <= n-m:
        if haystack[i:i+m] == needle:
            return i
        i += 1
    return -1

print(str_str("HelloWorld","or"))

