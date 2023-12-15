from collections import defaultdict


def happy_number(n):
    def find_squares(curr_num):
        result = 0

        while curr_num:
            digit = curr_num % 10
            digit = digit ** 2
            result += digit
            curr_num = curr_num // 10

        return result

    visited_nums = defaultdict(int)

    while n not in visited_nums:
        visited_nums[n] += 1
        n = find_squares(n)

        if n == 1:
            return True

    return False


res = happy_number(3)
print(res)
