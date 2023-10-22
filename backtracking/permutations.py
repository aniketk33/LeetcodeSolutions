"""understand the tree at this link https://www.youtube.com/watch?v=s7AvT7cGdSo,
so it will be easy to understand the recursive call"""


def permutations(num_arr):
    result = []
    if len(num_arr) == 1:
        return [num_arr[:]]

    for i in range(len(num_arr)):
        # pop the first number and then apply permutation on remaining nums
        first_num = num_arr.pop(0)
        permutation = permutations(num_arr)
        for perm in permutation:
            perm.append(first_num)
        result.extend(permutation)
        num_arr.append(first_num)

    return result


arr = [1, 2, 3]
res = permutations(arr)
print(res)
