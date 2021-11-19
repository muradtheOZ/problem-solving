
def isPalindrome(s):
    cleanString = ("".join([ c if c.isalnum() else "" for c in s ])).lower()
    revresed_clean_string = cleanString[::-1]
    if cleanString == revresed_clean_string:
        return True
    else:
        return False
s = "Ma. * Am"
print(isPalindrome(s))