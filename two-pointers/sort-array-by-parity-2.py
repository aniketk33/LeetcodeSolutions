def sort_array(nums):
    for idx, num in enumerate(nums):
        right = idx
        # for even index
        if idx % 2 == 0:
            # check if even value at that index
            if num % 2 != 0:
                while right < len(nums):
                    # get the next even value
                    if nums[right] % 2 == 0:
                        break
                    right += 1
                # swap values at the given index
                nums[idx], nums[right] = nums[right], nums[idx]
        else:
            if num % 2 == 0:
                # get the next odd value
                while right < len(nums):
                    if nums[right] % 2 != 0:
                        break
                    right += 1
                # swap values at the given index
                nums[idx], nums[right] = nums[right], nums[idx]

    return nums


# optimal approach
def sort_array_2(nums):
    even, odd = 0, 1

    while even < len(nums) and odd < len(nums):
        # moving the even pointer
        while even < len(nums) and nums[even] % 2 == 0:
            even += 2
        # moving the odd pointer
        while odd < len(nums) and nums[odd] % 2 != 0:
            odd += 2

        # swap places if the value at even or odd index is odd or even respective
        if even < len(nums) and odd < len(nums):
            nums[even], nums[odd] = nums[odd], nums[even]
            even += 2
            odd += 2

    return nums


# res = sort_array([4, 5, 7, 2])
res = sort_array_2([4, 5, 7, 2])
print(res)
