def subsets(num_arr):
    result = []
    curr_path = []

    def dfs(curr_idx):
        # if all the items are covered then add the path to the result
        if curr_idx >= len(num_arr):
            result.append(curr_path.copy())
            return

        # 1. add the num and then recursive call to dfs
        curr_path.append(num_arr[curr_idx])
        dfs(curr_idx + 1)

        # 2. pop the item and then recursive call to dfs
        curr_path.pop()
        dfs(curr_idx + 1)

    dfs(0)
    return result


nums = [1, 2, 3]
res = subsets(nums)
print(res)
