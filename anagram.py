def isAnagram(s, t):

    def sorted_string(value):
        making_tuple = ",".join(value)
        sorting_tuple = sorted(making_tuple)
        remove_otherthan_englishletter = ("".join([ c if c >= "a" and c<= "z" else "" for c in sorting_tuple ]))
        return remove_otherthan_englishletter

    sorted_string_one = sorted_string(s)
    sorted_string_two = sorted_string(t)

    if sorted_string_one == sorted_string_two:
        return True
    else:
        return False

a = "zsdikjlacxck"
b = "xckczsajldik"
print(isAnagram(a,b))