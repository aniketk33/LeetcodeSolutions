from calendar import leapdays
from collections import Counter, defaultdict
from typing import DefaultDict


def singleNumber(nums: list[int]) -> int:
    counter = Counter(nums)
    for i,j in reversed(counter.most_common()):
        if j==1:
            return i

dd = defaultdict(lambda: "not present")
dd["a"] = 1
dd["b"] = 1
print(dd["a"])
print(dd["b"])
print(dd["c"])
res = singleNumber([3,2,2,2,4,4])
print(list(range(11,0,-1)))
print(res)
'''Find the perfect number'''
# def checkPerfectNumber(n: int) -> bool:
#     res =[]
#     range_val = range(1, int(math.sqrt(n))+1)
#     for i in range_val:
#             if n%i==0:
#                 if i not in res:
#                     res.append(i)
#                 if n//i not in res:
#                     res.append(n//i)
#     s= sum(res)
#     return s==2*n

# res = checkPerfectNumber(28)
# print(res)