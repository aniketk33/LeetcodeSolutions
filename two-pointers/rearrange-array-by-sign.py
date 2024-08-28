# it fails for larger input size
def rearrange(nums):
    left, right = 0, 1

    while right < len(nums):
        # if left and right, both are positives
        if nums[left] > 0 and nums[right] > 0:
            # get the first negative index
            i = right
            while i < len(nums) and nums[i] > 0:
                i += 1
            # keep swapping until it reaches at the right index, to preserve the order
            while i > right:
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
                i -= 1
        # if left is negative and right is positive
        elif nums[left] < 0 < nums[right]:
            # swap their places
            nums[left], nums[right] = nums[right], nums[left]
        # if both are negatives
        elif nums[left] < 0 and nums[right] < 0:
            i = right
            # get the first positive value
            while i < len(nums) and nums[i] < 0:
                i += 1
            # keep swapping until it reaches at the left index, to preserve the order
            while i > left:
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
                i -= 1
        left += 2
        right += 2

    return nums


def rearrange_2(nums):
    positives, negatives = [n for n in nums if n > 0], [n for n in nums if n < 0]
    result = [0] * len(nums)
    idx = 0
    while 2 * idx < len(nums):
        result[2 * idx] = positives[idx]
        result[2 * idx + 1] = negatives[idx]
        idx += 1

    return result


# res = rearrange([3, 11, -47, 29, 18, -4, -26, 16, 15, -47, 4, -22, 41, -36, -27, -32])
res = rearrange_2([3, 11, -47, 29, 18, -4, -26, 16, 15, -47, 4, -22, 41, -36, -27, -32])
print(res)
