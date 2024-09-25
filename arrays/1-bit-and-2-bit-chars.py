def is_one_bit(bits):
    result = 0
    i = 0
    while i < len(bits):
        result = bits[i]
        if result == 1:
            result = result * 10 + bits[i + 1]
            i += 2
        else:
            i += 1

    return result == 0


# optimal approach
def is_one_bit_2(bits):
    i, n = 0, len(bits)

    while i < n - 1:
        i += 2 if bits[i] else 1
        # if bits[i] == 1:
        #     i += 2
        # else:
        #     i += 1

    # if the value is one bit, then the index will be n - 1 for sure
    return i == n - 1


# res = is_one_bit([1, 1, 1, 0])
res = is_one_bit_2([1, 1, 1, 0])
print(res)
