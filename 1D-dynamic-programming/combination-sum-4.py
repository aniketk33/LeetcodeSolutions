# using backtracking. it works but the time limit exceeds
def combination_sum(nums, target):
    count = 0

    def backtrack(curr_sum):
        if curr_sum > target:
            return

        nonlocal count
        if curr_sum == target:
            count += 1
            return

        for n in nums:
            curr_sum += n
            backtrack(curr_sum)
            curr_sum -= n

    backtrack(0)
    return count


def combination_sum_2(nums, target):
    cache = {0: 1}
    for count in range(1, target + 1):
        # initially, the count is zero
        cache[count] = 0
        for n in nums:
            cache[count] += cache.get(count - n, 0)

    return cache[target]


res = combination_sum_2([4, 2, 1], 32)
print(res)
