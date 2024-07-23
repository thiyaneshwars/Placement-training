def is_palindrome(x):
    if x < 0:
        return False
    rev = 0
    original = x
    while x:
        rev = rev * 10 + x % 10
        x //= 10
    return original == rev
