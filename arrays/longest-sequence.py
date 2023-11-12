def longest_sequence(nums):
    nums_set = set(nums)
    longest_seq = 0

    for num in nums:
        # check for its previous value in the set .i.e. to find the start of the sequence
        if (num - 1) not in nums_set:
            curr_seq_length = 0
            while (curr_seq_length + num) in nums_set:
                curr_seq_length += 1

            longest_seq = max(longest_seq, curr_seq_length)

    return longest_seq


input_nums = [100, 4, 200, 1, 3, 2]
res = longest_sequence(input_nums)
print(res)
