def longest_palindrome(s):
    res = ""
    for i in range(len(s)):
        for j in range(i, len(s)):
            substr = s[i:j + 1]
            if len(substr) > len(res) and substr == substr[::-1]:
                res = substr
    return res
