def teleport(arr1, arr2):
    # cannot be larger than this
    MODULO_AMT = 10 ** 9 + 7
    left, right = 0, 0
    # keeping track of the sum of each array
    arr1_sum, arr2_sum = 0, 0
    result = 0

    while left < len(arr1) and right < len(arr2):
        # NOTE: You will always encounter teleport numbers, so keep adding the smallest one
        if arr1[left] > arr2[right]:
            arr2_sum += arr2[right]
            right += 1
        elif arr1[left] < arr2[right]:
            arr1_sum += arr1[left]
            left += 1
        # teleport numbers matched
        else:
            arr1_sum += arr1[left]
            arr2_sum += arr2[right]
            result += max(arr1_sum, arr2_sum)
            result %= MODULO_AMT
            arr1_sum = 0
            arr2_sum = 0
            left += 1
            right += 1

    # fill the remaining numbers from both the arrays
    while left < len(arr1):
        arr1_sum += arr1[left]
        left += 1

    while right < len(arr2):
        arr2_sum += arr2[right]
        right += 1

    result += max(arr1_sum, arr2_sum)
    return result % MODULO_AMT


res = teleport([2, 4, 5, 8, 10], [4, 6, 8, 9])
print(res)
