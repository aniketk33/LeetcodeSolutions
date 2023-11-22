from collections import deque


def max_window(nums, window_size):
    left_ptr, right_ptr = 0, 0
    result = []
    q = deque()

    while right_ptr < len(nums):
        # pop all the smaller elements from the queue which were added previously
        while q and nums[q[-1]] < nums[right_ptr]:
            q.pop()

        q.append(right_ptr)

        # check if the left pointer is greater than the first value, which is the index, present in the queue
        if left_ptr > q[0]:
            q.popleft()

        # check for valid window size and add the number present at the start of the queue
        if right_ptr + 1 >= window_size:
            result.append(nums[q[0]])
            left_ptr += 1
        right_ptr += 1

    return result


res = max_window([1, 3, -1, -3, 5, 3, 6, 7], 3)
print(res)
