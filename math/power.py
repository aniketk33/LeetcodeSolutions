def find_pow(num1, exp):
    # return x**n
    def helper(x, n):
        # two edge cases
        if x == 0:
            return 0
        if n == 0:
            return 1

        result = helper(x * x, n // 2)
        if n % 2 == 0:
            return result
        else:
            return result * x

    power = helper(num1, abs(exp))
    return power if exp >= 0 else 1 / power


res = find_pow(2.0, -2)
print(res)
