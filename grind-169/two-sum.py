def two_sum(nums, target):
    compliments = {}

    for i in range(len(nums)):
        compliment = target - nums[i]
        # check if the compliment is present in the dict, and it is a different index
        if compliment in compliments and compliments[compliment] != i:
            return [i, compliments[compliment]]

        # store the index of the current number
        compliments[nums[i]] = i


res = two_sum([3, 2, 4], 6)
print(res)
