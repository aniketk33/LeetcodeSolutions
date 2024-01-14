def pairs(spells, potions, success):
    potions.sort()
    result = []

    for i in spells:
        # initialize with the length; when we don't find any possible pairs, the result should be zero
        count = len(potions)
        left_ptr, right_ptr = 0, len(potions) - 1
        while left_ptr <= right_ptr:
            mid = left_ptr + (right_ptr - left_ptr) // 2
            if i * potions[mid] >= success:
                count = mid
                right_ptr = mid - 1
            else:
                left_ptr = mid + 1
        result.append(len(potions) - count)

    return result


res = pairs([5, 1, 3], [1, 2, 3, 4, 5], 7)
print(res)
