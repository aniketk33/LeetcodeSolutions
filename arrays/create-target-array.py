def target_array(nums, index):
    result = []
    for i in range(len(nums)):
        if i == index[i]:
            result.append(nums[i])
        else:
            result.insert(index[i], nums[i])

    return result


res = target_array([0, 1, 2, 3, 4], [0, 1, 2, 2, 1])
print(res)
