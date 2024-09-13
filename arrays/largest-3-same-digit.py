def largest_digit(num):
    max_num = 0
    result = ''
    left = 0

    for right in range(2, len(num)):
        curr_window = num[left:right + 1]
        if len(set(curr_window)) == 1:
            if int(curr_window) >= max_num:
                max_num = int(curr_window)
                result = curr_window
        left += 1

    return result


# logical solution
def largest_digit_2(num):
    # there can be only these valid pairs in any given solution
    good_ints = ['999', '888', '777', '666', '555', '444', '333', '222', '111', '000']

    for good in good_ints:
        if good in num:
            return good
    return ""


res = largest_digit('6777133339')
print(res)
