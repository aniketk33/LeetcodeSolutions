def check_valid(nums):
    cache = {}

    def dfs(curr_idx):
        if curr_idx == len(nums):
            return True

        if curr_idx in cache:
            return cache[curr_idx]

        valid_partition = False
        # check if two consecutive values are the same. '- 1' is added because to check if at least 2 nums are present
        if curr_idx < len(nums) - 1 and nums[curr_idx] == nums[curr_idx + 1]:
            valid_partition = dfs(curr_idx + 2)

        # check if at least 3 nums present
        if curr_idx < len(nums) - 2:
            if (nums[curr_idx] == nums[curr_idx + 1] == nums[curr_idx + 2]) or (
                    nums[curr_idx] + 1 == nums[curr_idx + 1] == nums[curr_idx + 2] - 1):
                valid_partition = valid_partition or dfs(curr_idx + 3)

        cache[curr_idx] = valid_partition

        return valid_partition

    return dfs(0)


res = check_valid([4, 4, 4, 5, 6])
print(res)
