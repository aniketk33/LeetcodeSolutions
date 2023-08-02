"""Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Examples

Example 1:

Input: aab

Output:

[
["aa","b"],
["a","a","b"]
]
"""
from typing import List


def partition(s: str) -> List[List[str]]:
    result = []

    def is_palindrome(st):
        return st == st[::-1]

    def dfs(take, remain, path):
        if len(remain) == 0:
            if len(path) > 0:
                result.append(path[:])
            return

        for index, value in enumerate(remain):
            take = remain[0:index + 1]
            new_remain = remain[index + 1:]

            if is_palindrome(take):
                path.append(take)
                dfs(take, new_remain, path)
                path.pop()

    dfs("", s, [])

    return result


input_str = 'aab'
res = partition(input_str)
print(res)
