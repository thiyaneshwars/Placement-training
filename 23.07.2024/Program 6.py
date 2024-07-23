def convert(s, num_rows):
    if num_rows == 1:
        return s
    rows = [""] * min(num_rows, len(s))
    cur_row = 0
    going_down = False
    for char in s:
        rows[cur_row] += char
        if cur_row == 0 or cur_row == num_rows - 1:
            going_down = not going_down
        cur_row += 1 if going_down else -1
    return "".join(rows)
