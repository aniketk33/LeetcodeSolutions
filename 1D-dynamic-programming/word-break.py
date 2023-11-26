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

    def dfs(curr_idx):
        # check if the current index is equal to the target's length
        if curr_idx == len(target):
            return True

        if curr_idx in memo:  # memoization
            return memo[curr_idx]

        ans = False  # initial value
        for word in words_arr:
            # if target[curr_idx:].startswith(word):
            if target[curr_idx: curr_idx + len(word)] == word:
                if dfs(curr_idx + len(word)):
                    ans = True
                    break

        memo[curr_idx] = ans
        return ans

    return dfs(0)


arr = ["neet", "leet", "code"]
tar = 'leetcode'
res = word_break(arr, tar)
print(res)
