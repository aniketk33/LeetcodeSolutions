"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

You can provide input as 'abc' or list of nums as [1,2,3], it will return the valid output
"""

from typing import List


def permutations(letters):
    def dfs(start_idx: int, path: List[str], used_letter: List[bool], res: List[str]):
        if start_idx == len(letters):
            # res.append(''.join(path))
            result.append(path[:])
            return
        for i, letter in enumerate(letters):
            if used_letter[i]:
                continue
            path.append(letter)
            used_letter[i] = True
            dfs(start_idx + 1, path, used_letter, res)
            path.pop()
            used_letter[i] = False

    result = []
    dfs(0, [], [False] * len(letters), result)
    return result


input_str = [1, 2, 3]
output = permutations(input_str)
print(output)
