'''A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
A self-dividing number is not allowed to contain the digit zero.

Given two integers left and right, return a list of all the self-dividing numbers in the range [left, right].'''

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        result_nums = []
        # range for loop for start and end position
        for num in range(left, right+1):
            # check if it contains zero then skip the number
            if num.__str__().__contains__('0'):
                continue
            temp_num = num
            while temp_num != 0:
                last_digit = temp_num % 10
                if num % last_digit != 0:
                    break
                temp_num //= 10
            if temp_num == 0:
                result_nums.append(num)
        
        return result_nums

left = 1
right = 22
soln = Solution().selfDividingNumbers(left, right)
print(soln)