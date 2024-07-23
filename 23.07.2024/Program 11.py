def roman_to_int(s):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0
    for char in s:
        curr_value = roman[char]
        if curr_value > prev_value:
            total += curr_value - 2 * prev_value
        else:
            total += curr_value
        prev_value = curr_value
    return total
