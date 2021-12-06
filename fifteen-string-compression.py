def compress(chars):
    n = len(chars)
    current_indx = 1
    previous_char = chars[0]
    count = 1

    i = 1

    while i < n:
        if chars[i] == previous_char:
            count += 1
        else:
            if count > 1:
                temp_s = str(count)
                for ch in temp_s:
                    chars[current_indx] =ch
                    current_indx += 1
            previous_char = chars[i]
            chars[current_indx] = chars[i] 
            current_indx += 1
            count = 1
        i += 1
    if count > 1:
        temp_s = str(count)
        for ch in temp_s:
            chars[current_indx] =ch
            current_indx += 1
    return current_indx
print(compress(["a","a","b","b","c","c","c"]))


