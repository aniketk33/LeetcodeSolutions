'''You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".

'''
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_count = 0
        jewels_unique = set(jewels)
        for stone in stones:
            if stone not in jewels_unique:
                continue
            jewel_count += 1
        
        return jewel_count

jewels = "zz"
stones = "ZZZ"
soln = Solution().numJewelsInStones(jewels, stones)
print(soln)