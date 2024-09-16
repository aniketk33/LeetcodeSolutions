def plus_one(digits_arr):
    arr_len = len(digits_arr)
    carry = 0
    # last digit operation
    last_digit = digits_arr[-1]
    last_digit = carry + last_digit + 1
    carry = last_digit // 10
    last_digit %= 10
    digits_arr[-1] = last_digit
    if carry:
        for i in range(arr_len - 2, -1, -1):
            last_digit = digits_arr[i]
            last_digit = carry + last_digit
            carry = last_digit // 10
            last_digit %= 10
            digits_arr[i] = last_digit
        if carry:
            digits_arr.insert(0, carry)

    return digits_arr


def plus_one_2(digits):
    carry = 1
    digits.reverse()
    idx = 0

    while carry:
        if idx < len(digits):
            if digits[idx] == 9:
                digits[idx] = 0
            else:
                digits[idx] += 1
                carry = 0
            idx += 1
        else:
            digits.append(1)
            carry = 0
    digits.reverse()

    return digits


# res = plus_one([9, 9, 9])
res = plus_one_2([9, 9, 9])
print(res)
