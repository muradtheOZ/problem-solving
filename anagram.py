def isAnagram(s, t):

    def sorted_string(value):
        sorting_tuple = sorted(value)
        return sorting_tuple

    sorted_string_one = sorted_string(s)
    sorted_string_two = sorted_string(t)

    if sorted_string_one == sorted_string_two:
        return True
    else:
        return False

a = "zsdikjlacxcklk"
b = "xckczsajldiklk"
print(isAnagram(a,b))