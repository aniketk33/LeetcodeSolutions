import random


class RandomizedSet:

    def __init__(self):
        self.map_numbers = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        is_present = val not in self.nums
        if is_present:
            self.nums.append(val)
            # store the added number with the index position
            self.map_numbers[val] = len(self.nums) - 1

        return is_present

    def remove(self, val: int) -> bool:
        is_present = val in self.nums
        if is_present:
            # check for it's index
            idx = self.map_numbers[val]
            # shift the last element to the removed element's position
            last_element = self.nums[-1]
            self.nums[idx] = last_element
            self.nums.pop()
            # update the last element's index value in the hash map
            self.map_numbers[last_element] = idx
            # delete the value from the hash map
            del self.map_numbers[val]
        return is_present

    def getRandom(self) -> int:
        return random.choice(self.nums)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
