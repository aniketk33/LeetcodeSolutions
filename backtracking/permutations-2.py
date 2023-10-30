def permutations_2(num_arr):
    # create hashmap to store the count of each num
    count_dict = {n: 0 for n in num_arr}
    for n in num_arr:
        count_dict[n] += 1

    result, curr_permutations = [], []

    # BACKTRACK
    def dfs():
        # add to the result if length matches the input array size
        if len(curr_permutations) == len(num_arr):
            result.append(curr_permutations[::])
            return

        # create permutations of keys
        for num in count_dict:
            # check if count is greater than 0 to add them in the current permutation list
            if count_dict[num] > 0:
                # add and decrease the count
                curr_permutations.append(num)
                count_dict[num] -= 1
                dfs()
                # remove and increase the count
                curr_permutations.pop()
                count_dict[num] += 1

    dfs()
    return result


nums = [1, 1, 2]
res = permutations_2(nums)
print(res)
