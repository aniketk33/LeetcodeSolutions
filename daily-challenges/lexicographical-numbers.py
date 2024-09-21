def lexicographical(n):
    order = {}

    for i in range(1, n + 1):
        if i > 9:
            result = ''
            num = i
            while num > 0:
                remainder = num % 10
                result = str(ord(str(remainder))) + result
                num = num // 10
            order[i] = result
        else:
            order[i] = str(ord(str(i)))

    return [*dict(sorted(order.items(), key=lambda x: x[1])).keys()]


def lexicographical_2(n):
    return sorted(range(1, n + 1), key=str)


# optimal solution
def lexicographical_3(n):
    result = []
    curr_num = 1

    while len(result) < n:
        result.append(curr_num)

        # move to the next child
        if curr_num * 10 <= n:
            curr_num *= 10
        else:
            # only pop when it is equal to n or the last digit is 9
            while curr_num == n or curr_num % 10 == 9:
                curr_num = curr_num // 10
            curr_num += 1

    return result


# res = lexicographical(10)
# res = lexicographical_2(10)
res = lexicographical_3(13)
print(res)
