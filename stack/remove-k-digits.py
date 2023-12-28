def remove_digits(num, k):
    stack = []

    for n in num:
        while stack and k > 0 and stack[-1] > n:
            stack.pop()
            k -= 1

        stack.append(n)

    # removing leading zeros
    i = 0
    while i < len(stack) and stack[i] == "0":
        i += 1

    # if the k is still greater than 0
    while k and stack:
        stack.pop()
        k -= 1

    result = ''.join(stack[i:])
    return result or "0"


res = remove_digits('10200', 1)
print(res)
