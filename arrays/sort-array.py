def sort_array(nums):
    def merge_sort(left_idx, right_idx):
        if left_idx >= right_idx:
            return

        mid_idx = left_idx + (right_idx - left_idx) // 2
        # divide the array into two halves
        merge_sort(left_idx, mid_idx)
        merge_sort(mid_idx + 1, right_idx)

        # merge the divided halves
        merge_array(left_idx, mid_idx, right_idx)

    def merge_array(left_idx, mid_idx, right_idx):
        temp_result = []
        # first index of the first half array
        curr_left = left_idx

        # first index of the second half array
        curr_right = mid_idx + 1

        # out-of-bounds check
        while curr_left <= mid_idx and curr_right <= right_idx:
            if nums[curr_left] <= nums[curr_right]:
                temp_result.append(nums[curr_left])
                curr_left += 1
            else:
                temp_result.append(nums[curr_right])
                curr_right += 1

        # check if elements are still left from both the halves

        while curr_left <= mid_idx:
            temp_result.append(nums[curr_left])
            curr_left += 1

        while curr_right <= right_idx:
            temp_result.append(nums[curr_right])
            curr_right += 1

        # to replace the result's array value with the sorted values in the temp_result array
        for i in range(left_idx, right_idx + 1):
            # each time the temp_result will be re-initialized,
            # and the first element will be at index 0, but the left_idx will not be zero everytime,
            # say it is 2. the loop will begin from 2 to right_ix, thus, obtaining the 0th index value
            # of temp_result, subtract the 'i' with 'left_idx'. 2-2 =0. 3-2=1 and so on
            nums[i] = temp_result[i - left_idx]

    merge_sort(0, len(nums) - 1)


arr = [5, 2, 3, 1]
print(f'Before sorting: {arr}')
sort_array(arr)
print(f'After sorting: {arr}')
