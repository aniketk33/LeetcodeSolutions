# brute force approach. TLE
def closest(nums, target):
    diff = float('inf')
    result = 0
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                curr_sum = nums[i] + nums[j] + nums[k]
                if diff > abs(curr_sum - target):
                    diff = abs(curr_sum - target)
                    result = curr_sum

    return result


# optimal solution
def closest_2(nums, target):
    nums.sort()
    result = float('inf')

    for i, val in enumerate(nums):
        left, right = i + 1, len(nums) - 1
        while left < right:
            curr_sum = val + nums[left] + nums[right]

            if curr_sum == target:
                return curr_sum
            # store the min diff between the current sum and result with target
            if abs(curr_sum - target) < abs(result - target):
                result = curr_sum

            # move pointers
            if curr_sum > target:
                right -= 1
            else:
                left += 1

    return result


# res = closest([-1, 2, 1, -4], 1)
res = closest_2([-1, 2, 1, -4], 1)
print(res)
