from collections import Counter, defaultdict


# brute force approach. TLE and also wrong answer for the last few test cases
def divisible_pairs(arr, k):
    count = 0
    num_count = Counter(arr)

    for i in range(len(arr)):
        if num_count[arr[i]] <= 0:
            continue
        for j in range(i + 1, len(arr)):
            curr_val = arr[j]
            if num_count[curr_val] > 0 and (curr_val + arr[i]) % k == 0:
                count += 1
                num_count[curr_val] -= 1
                num_count[arr[i]] -= 1
                break

    return count == len(arr) / 2


def divisible_pairs_2(arr, k):
    remainder_count = defaultdict(int)
    for num in arr:
        # to handle negative remainders
        remainder = (num % k + k) % k
        remainder_count[remainder] += 1

    if remainder_count[0] % 2 != 0:
        return False

    # remainder values is always in the range of 0..k-1
    for i in range(1, k // 2 + 1):
        compliment_remainder = k - i
        if remainder_count[compliment_remainder] != remainder_count[i]:
            return False

    return True


# res = divisible_pairs([1, 2, 3, 4, 5, 10, 6, 7, 8, 9], 5)
# res = divisible_pairs_2([1, 2, 3, 4, 5, 10, 6, 7, 8, 9], 5)
res = divisible_pairs_2([3, 8, 17, 2, 5, 6], 10)
print(res)
