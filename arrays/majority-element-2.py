from collections import Counter


# solution using extra space O(n)
def majority(nums):
    count = Counter(nums)
    n = len(nums) / 3
    result = []

    for k, v in count.items():
        if v > n:
            result.append(k)

    return result


# using constant space
def majority_2(nums):
    count1 = count2 = 0
    num1 = num2 = None
    n = len(nums)

    for num in nums:
        if num == num1:
            count1 += 1
        elif num == num2:
            count2 += 1
        elif count1 == 0:
            num1 = num
            count1 = 1
        elif count2 == 0:
            num2 = num
            count2 = 1
        else:
            count1 -= 1
            count2 -= 1

    count1 = count2 = 0
    for num in nums:
        if num == num1:
            count1 += 1
        elif num == num2:
            count2 += 1

    result = []
    if count1 > (n // 3):
        result.append(num1)
    if count2 > (n // 3):
        result.append(num2)

    return result


# res = majority([3, 2, 3])
res = majority_2([3, 2, 3, 4, 4])
print(res)
