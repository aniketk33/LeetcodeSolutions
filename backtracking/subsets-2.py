def subsets_two(num_arr):
    result = []
    num_arr.sort()

    def backtrack(curr_idx, curr_subset):
        if curr_idx == len(num_arr):
            result.append(curr_subset[::])
            return

        # add the num and recursive call
        curr_subset.append(num_arr[curr_idx])
        backtrack(curr_idx + 1, curr_subset)
        curr_subset.pop()

        # skip the duplicates
        while curr_idx + 1 < len(num_arr) and num_arr[curr_idx] == num_arr[curr_idx + 1]:
            curr_idx += 1

        # call recursively on non-duplicates
        backtrack(curr_idx + 1, curr_subset)

    backtrack(0, [])
    return result


arr = [1, 2, 2]
res = subsets_two(arr)
print(res)
