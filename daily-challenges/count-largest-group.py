from collections import defaultdict


def count_largest(n):
    # digit sum dict
    digit_sum = defaultdict(int)

    for num in range(1, n + 1):
        curr_sum = 0
        while num > 0:
            remainder = num % 10
            curr_sum += remainder
            num = num // 10
        digit_sum[curr_sum] += 1

    max_val = 0
    count = 0
    for val in digit_sum.values():
        if val > max_val:
            max_val = val

    for val in digit_sum.values():
        if max_val == val:
            count += 1

    return count


res = count_largest(13)
print(res)
