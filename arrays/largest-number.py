from functools import cmp_to_key


def largest_number(nums):
    # convert to string
    for i, num in enumerate(nums):
        nums[i] = str(num)

    def compare(n1, n2):
        return -1 if n1 + n2 > n2 + n1 else 1

    nums = sorted(nums, key=cmp_to_key(compare))
    # for a case such as "000" it should return only 0 therefore, convert to int first then return as a string object
    return str(int(''.join(nums)))


res = largest_number([10, 2])
print(res)
