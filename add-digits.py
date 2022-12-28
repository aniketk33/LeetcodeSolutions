'''Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.'''
class Solution:
    def addDigits(self, num: int) -> int:
        result = 0
        while num > 0:
            result += num % 10
            num = num // 10
            
            if num == 0 and result > 9:
                num = result
                result = 0
                
        return result

soln = Solution().addDigits(38)
print(soln)