def combination_sum_two(num_arr, target):
    num_arr.sort()
    result = []

    def backtrack(curr_idx, curr_path, curr_sum):
        if curr_sum == 0:
            result.append(curr_path.copy())
        if curr_sum <= 0:
            return

        prev_num = -1
        for i in range(curr_idx, len(num_arr)):
            if prev_num == num_arr[i]:
                continue
            curr_path.append(num_arr[i])
            backtrack(i + 1, curr_path, curr_sum - num_arr[i])
            curr_path.pop()

            prev_num = num_arr[i]

    backtrack(0, [], target)
    return result


candidates = [10, 1, 2, 7, 6, 1, 5]
res = combination_sum_two(candidates, 8)
print(res)
