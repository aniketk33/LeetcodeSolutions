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
    char_arr = list(s)
    if len(char_arr) == 1:
        return sym_val_dict.get(char_arr[0])
    left_ptr, right_ptr = 0, 1
    result = 0
    while right_ptr < len(char_arr):
        left_val = sym_val_dict.get(char_arr[left_ptr])
        right_val = sym_val_dict.get(char_arr[right_ptr])
        result += (left_val if left_val > right_val else -left_val)
        left_ptr += 1
        right_ptr += 1

    result += sym_val_dict.get(char_arr[left_ptr])  # append the last value
    return result


input_s = "MCMXCIV"
res = roman_to_int(input_s)
print(res)
