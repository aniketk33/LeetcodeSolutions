class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s, t = sorted(s), sorted(t)
        return t[-1] if s == t[:-1] else [x[1] for x in zip(s, t) if x[0] != x[1]][0]

s = "abcd"
t = "abcde"
soln = Solution()
result = soln.findTheDifference(s, t)
print(result)