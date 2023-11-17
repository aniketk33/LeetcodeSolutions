def four_sum(nums, target):
    nums.sort()
    result = []
    curr_combination = []

    def k_sum(k, start_idx, curr_target):
        # for k greater than 2
        if k != 2:
            # we will exclude the last two elements when we recursively call the k_sum function
            for i in range(start_idx, len(nums) - k + 1):
                # check if the previous element is the same as the current
                if i > start_idx and nums[i] == nums[i - 1]:
                    continue
                curr_combination.append(nums[i])
                k_sum(k - 1, i + 1, curr_target - nums[i])
                curr_combination.pop()
            return

        # applying two-sum techniques to get the target value
        left_ptr, right_ptr = start_idx, len(nums) - 1
        while left_ptr < right_ptr:
            if nums[left_ptr] + nums[right_ptr] < curr_target:
                left_ptr += 1
            elif nums[left_ptr] + nums[right_ptr] > curr_target:
                right_ptr -= 1
            else:
                result.append(curr_combination + [nums[left_ptr], nums[right_ptr]])
                left_ptr += 1
                # EDGE CASE: while shifting the left pointer, if we encounter the same next value,
                # we have to keep moving the left pointer until we find the next unique value
                while left_ptr < right_ptr and nums[left_ptr] == nums[left_ptr - 1]:
                    left_ptr += 1

    k_sum(4, 0, target)
    return result


res = four_sum([1, 0, -1, 0, -2, 2], 0)
print(res)
