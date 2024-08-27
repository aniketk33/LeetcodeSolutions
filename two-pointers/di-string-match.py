def di_match(s):
    count_i, count_d = 0, len(s)
    result = [0] * (len(s) + 1)
    curr_idx = 0
    for char in s:
        if char == 'I':
            result[curr_idx] = count_i
            count_i += 1
        else:
            result[curr_idx] = count_d
            count_d -= 1
        curr_idx += 1
    # append the value of count_i at the end
    result[-1] = count_i

    return result


res = di_match('IDID')
print(res)
