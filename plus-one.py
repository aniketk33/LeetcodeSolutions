"""66. You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's. Increment the large integer by one and return the resulting array of digits.
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
"""


def plus_one(digits_arr):
    arr_len = len(digits_arr)
    carry = 0
    # last digit operation
    last_digit = digits_arr[-1]
    last_digit = carry + last_digit + 1
    carry = last_digit // 10
    last_digit %= 10
    digits_arr[-1] = last_digit
    if carry:
        for i in range(arr_len - 2, -1, -1):
            last_digit = digits_arr[i]
            last_digit = carry + last_digit
            carry = last_digit // 10
            last_digit %= 10
            digits_arr[i] = last_digit
        if carry:
            digits_arr.insert(0, carry)


arr = [9, 9, 9]
plus_one(arr)
print(arr)
