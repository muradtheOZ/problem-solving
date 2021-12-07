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
        if a[i] == "0" and b[i] == "0":
            result = 0 + carry
            carry = 0
        elif a[i] == "1" and b[i] == "1":
            result = 0 + carry
            carry = 1
        else:
            result = 1 + carry 
            if result == 2:
                result = 0
                carry = 1
        output.append(result)

    if carry == 1:
        output.append(carry)
    pre_string =  "".join([str(i)for i in output])
    final_string = pre_string[::-1]
    return final_string

print(add_binary("1010","1011"))
    
        