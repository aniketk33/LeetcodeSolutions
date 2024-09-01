sym_val_dict = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}


def roman_to_int(s):
    # char_arr = list(s)
    if len(s) == 1:
        return sym_val_dict[s[0]]
    left_ptr, right_ptr = 0, 1
    result = 0
    while right_ptr < len(s):
        left_val = sym_val_dict[s[left_ptr]]
        right_val = sym_val_dict[s[right_ptr]]

        # append negative left value when it is smaller than right value
        if left_val >= right_val:
            result += left_val
        else:
            result -= left_val

        left_ptr += 1
        right_ptr += 1

    result += sym_val_dict[s[left_ptr]]  # append the last value
    return result


def roman_to_int_2(s):
    result = 0
    prev = s[-1]
    for i in range(len(s)-1, -1, -1):
        curr = s[i]
        if sym_val_dict[prev] > sym_val_dict[curr]:
            result -= sym_val_dict[curr]
        else:
            result += sym_val_dict[curr]
        prev = curr

    return result


input_s = "III"
# res = roman_to_int(input_s)
res = roman_to_int_2(input_s)
print(res)
