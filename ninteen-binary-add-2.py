def add_binary(a,b):
    a = a[::-1]
    b = b[::-1]

    len_a,len_b = len(a),len(b)
    if len_a < len_b:
        a = a + "0"*(len_b-len_a)
    elif len_b < len_a:
        b = b + "0"*(len_a - len_b)
    output = []
    carry = 0
     
    for i in range (len(a)):
        carry , result = divmod((ord(a[i])-48) + (ord(b[i])-48) + carry,2)
        output.append(str(result))

    if carry == 1:
        output.append(str(carry))
    return "".join(output[::-1])

print(add_binary("1010","1011"))
    
        