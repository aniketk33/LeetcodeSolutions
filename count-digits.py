def count_digits(n):
    original_num = n
    count = 0

    while n > 0:
        curr_num = n % 10
        if original_num % curr_num == 0:
            count += 1
        n //= 10

    return count


res = count_digits(336)
print(res)
