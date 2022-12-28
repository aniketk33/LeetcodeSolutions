'''Input: candyType = [1,1,2,2,3,3]
Output: 3
Explanation: Alice can only eat 6 / 2 = 3 candies. Since there are only 3 types, she can eat one of each type.
'''
class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        candy_types = len(set(candyType))
        candy_len = len(candyType)//2
        return candy_types if candy_types < candy_len else candy_len

candyType = [6,6,6,6]
soln = Solution().distributeCandies(candyType)
print(soln)