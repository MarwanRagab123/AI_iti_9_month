import re
def is_palindrome(s):
    s = re.sub(r'[^A-Za-z0-9]', '', s).lower()
    return s == s[::-1]

s=" "
print(is_palindrome(s))