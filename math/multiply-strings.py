def multiply(num1, num2):
    if "0" in [num1, num2]:
        return "0"

    result = [0] * (len(num1) + len(num2))
    # reverse the number to avoid trailing zeros
    num1, num2 = num1[::-1], num2[::-1]

    for idx1 in range(len(num1)):
        for idx2 in range(len(num2)):
            value = int(num1[idx1]) * int(num2[idx2])
            # store the result
            result[idx1 + idx2] += value
            # move the carry to the next index
            result[idx1 + idx2 + 1] += result[idx1 + idx2] // 10
            # mod the calculated value to get the 10's position
            result[idx1 + idx2] = result[idx1 + idx2] % 10

    # reverse the calculated value
    result = result[::-1]
    zeroes = 0
    # calculate the leading zeroes
    while zeroes < len(result) and result[zeroes] == 0:
        zeroes += 1

    # convert to string
    result = map(str, result[zeroes:])
    return ''.join(result)


res = multiply("909", "99")
print(res)
