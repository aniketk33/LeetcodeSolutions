def max_area(height_arr):
    max_container_area = 0

    left, right = 0, len(height_arr) - 1

    while left < right:
        # get the min height
        height = min(height_arr[left], height_arr[right])
        length = right - left
        # current area
        area = length * height
        max_container_area = max(max_container_area, area)
        if height_arr[left] < height_arr[right]:
            left += 1
        else:
            right -= 1

    return max_container_area


res = max_area([1, 8, 6, 2, 5, 4, 8, 3, 7])
print(res)
