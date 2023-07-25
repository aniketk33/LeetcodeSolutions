def contains_duplicate(num_arr: list):
    """Time and Space complexity is O(n)"""
    count = set()
    for n in num_arr:
        if n in count:
            return True
        count.add(n)

    return False


def contains_duplicate_2(num_arr: list):
    """Using 2 pointer approach. Time complexity is O(nlog(n)) but space complexity is O(1)"""
    num_arr.sort()
    left_ptr, right_ptr = 0, 1
    while right_ptr < len(num_arr):
        if num_arr[left_ptr] == num_arr[right_ptr]:
            return True
        left_ptr += 1
        right_ptr += 1

    return False


nums = [1, 2, 3, 4]
# nums = [274, -735, -911, 80, 454, -511, 922, -775, 985, -669, -463, -896, -629, -586, 910, -361, 288, -375, 88, 556,
#         -578, -406, -87, 25, 377, -635, -445, -289, 646, -962, -487, -924, -968, -962, 502, 36, 129, -611, 54, -27,
#         -496, 915, -84, -782, 349, 678, 332, -114, 345, 14, 119, 710, 821, -194, 988, 38, -369, 409, -559, -529, -298,
#         -593, 705]
res = contains_duplicate_2(nums)
print(res)
