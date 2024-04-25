def reverse(num):
    reversed_num = 0
    is_negative = False
    if num < 0:
        is_negative = True
        num *= -1

    while num > 0:
        remainder = num % 10
        reversed_num = reversed_num * 10 + remainder
        num //= 10

    if reversed_num < -2**31 or reversed_num > 2**31-1:
        return 0

    return -reversed_num if is_negative else reversed_num


res = reverse(1534236469)
print(res)
