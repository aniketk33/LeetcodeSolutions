class RemoveElement:
    def removeElement(self, nums: list, val) -> int:
        duplicate_count = 0
        for num in reversed(nums):
            if val != num:
                continue
            duplicate_count += 1
            nums.remove(num)
        return len(nums)
        
input = [0,1,2,2,3,0,4,2]
num = 2
op = RemoveElement().removeElement(input, num)
print(op)