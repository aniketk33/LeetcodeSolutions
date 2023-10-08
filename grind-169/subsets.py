def subsets(nums):
    result = []

    def dfs(start_idx, path):
        result.append(path[:])
        for i in range(start_idx, len(nums)):
            path.append(nums[i])
            dfs(i + 1, path)
            path.pop()

    dfs(0, [])
    return result


arr = [1, 2, 3]
res = subsets(arr)
print(res)
