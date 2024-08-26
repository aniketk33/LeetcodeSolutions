def duplicate(arr):
    left = 0
    while left < len(arr):
        # for zero, add to the next index and pop the last element and then increment the counter
        if arr[left] == 0:
            arr.insert(left + 1, 0)
            arr.pop()
            left += 1
        # increment the left pointer as usual
        left += 1


def duplicate_2(arr):
    zeroes = arr.count(0)
    n = len(arr)
    right = n - 1

    while right >= 0:
        if zeroes + right < n:
            # at the last index assign the current value
            arr[zeroes + right] = arr[right]

        # if the current value is zero, then decrease the zero count and add an extra zero before it
        if arr[right] == 0:
            zeroes -= 1
            if zeroes + right < n:
                arr[zeroes + right] = 0

        right -= 1


nums = [1, 0, 2, 3, 0, 4, 5, 0]
print(f'Array: {nums}')
# duplicate(nums)
duplicate_2(nums)
print(f'Array: {nums}')
