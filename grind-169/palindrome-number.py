def is_palindrome(num):
    res = 0
    original_num = num
    while num > 0:
        res = res * 10 + num % 10
        num //= 10

    return original_num == res


n = 121
result = is_palindrome(n)
print(result)
