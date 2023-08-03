"""Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.


Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.

"""


def combine(n, k):
    result = []

    def dfs(start_idx, path):
        if len(path) == k:
            result.append(path[:])
            return

        for i in range(start_idx, n + 1):
            path.append(i)
            dfs(i + 1, path)
            path.pop()

    dfs(1, [])
    return result


res = combine(4, 2)
print(res)
