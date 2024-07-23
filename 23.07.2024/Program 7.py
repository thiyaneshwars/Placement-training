def reverse(x):
    sign = -1 if x < 0 else 1
    x *= sign
    rev = 0
    while x:
        rev = rev * 10 + x % 10
        x //= 10
    return sign * rev if rev.bit_length() < 32 else 0
