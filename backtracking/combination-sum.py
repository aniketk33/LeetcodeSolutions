def combination_sum(num_arr, target):
    result = []

    def dfs(curr_idx, curr_path, curr_total):
        # add the nums in the path
        if curr_total == target:
            result.append(curr_path.copy())
            return

        # out of bound case
        if curr_idx >= len(num_arr) or curr_total > target:
            return

        # 1. include duplicates i.e keep including itself
        curr_path.append(num_arr[curr_idx])
        # curr_idx won't change as we are adding the same number recursively
        dfs(curr_idx, curr_path, curr_total + num_arr[curr_idx])

        # 2. include a unique number
        curr_path.pop()
        # curr_total will remain the same as we have popped the last item from the list
        dfs(curr_idx + 1, curr_path, curr_total)

    dfs(0, [], 0)
    return result


candidates = [2, 3, 6, 7]
tar = 7
res = combination_sum(candidates, tar)
print(res)
