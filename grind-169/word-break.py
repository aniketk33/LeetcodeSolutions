"""Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated
sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
"""
from typing import List


def word_break(words_arr: List[str], target: str):
    memo = {}  # for memoization

    def dfs(start_idx):
        if start_idx == len(target):
            return True

        if start_idx in memo:  # memoization
            return memo[start_idx]

        ans = False  # initial value
        for word in words_arr:
            if target[start_idx:].startswith(word):
                if dfs(start_idx + len(word)):
                    ans = True
                    break

        memo[start_idx] = ans
        return ans

    return dfs(0)


arr = ["leet", "code"]
tar = 'leetcode'
res = word_break(arr, tar)
print(res)
