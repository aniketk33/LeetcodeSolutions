import heapq


def min_avg(nums):
    nums.sort()
    average_heap = []
    left, right = 0, len(nums) - 1

    while left < right:
        avg = (nums[left] + nums[right]) / 2
        average_heap.append(avg)
        left += 1
        right -= 1

    heapq.heapify(average_heap)
    return heapq.heappop(average_heap)


def min_avg_2(nums):
    nums.sort()
    # num cannot be greater than 50 (given in the constraint)
    result = 51
    left, right = 0, len(nums) - 1

    while left < right:
        avg = (nums[left] + nums[right]) / 2
        if result > avg:
            result = avg
        left += 1
        right -= 1

    return result


# res = min_avg([7, 8, 3, 4, 15, 13, 4, 1])
res = min_avg_2([7, 8, 3, 4, 15, 13, 4, 1])
print(res)
