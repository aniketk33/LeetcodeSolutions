"""A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1" 'B' -> "2" ... 'Z' -> "26" To decode an encoded message, all the digits must be grouped then mapped back
into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped
into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The test cases are generated so that the answer fits in a 32-bit integer.



Example 1:

Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

"""


def decode_digits(digits: str):
    memo = {}  # memoization

    def dfs(start_idx):
        if start_idx in memo:
            return memo[start_idx]

        if start_idx == len(digits):  # return if a way has been found to decode
            return 1

        ways = 0
        if digits[start_idx] == '0':  # check if leading zeros are present
            return ways

        # call when encounter a single digit
        ways += dfs(start_idx + 1)
        # for double digits
        if 10 <= int(digits[start_idx:start_idx + 2]) <= 26:
            ways += dfs(start_idx + 2)

        memo[start_idx] = ways
        return ways

    return dfs(0)


# bottom-up approach
def decode_digits_2(digits):
    memo = {len(digits): 1}
    for i in range(len(digits) - 1, -1, -1):
        # check if leading zeros
        if digits[i] == "0":
            memo[i] = 0
        else:
            memo[i] = memo[i + 1]

        if i + 1 < len(digits) and (digits[i] == "1" or digits[i] == "2" and digits[i + 1] in "0123456"):
            memo[i] += memo[i + 2]

    return memo[0]


d = '12'
res = decode_digits_2(d)
print(res)
