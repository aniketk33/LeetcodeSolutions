class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None


class MyHashSet:

    # def __init__(self):
    #     self.hash_set = []
    #
    # def add(self, key: int) -> None:
    #     if key in self.hash_set:
    #         return
    #     self.hash_set.append(key)
    #
    # def remove(self, key: int) -> None:
    #     if key not in self.hash_set:
    #         return
    #     self.hash_set.remove(key)
    #
    # def contains(self, key: int) -> bool:
    #     return key in self.hash_set

    # HASHTABLE SOLUTION
    def __init__(self):
        self.hash_table = [ListNode(0) for _ in range(10 ** 6)]

    def add(self, key: int) -> None:
        idx = key % len(self.hash_table)
        curr = self.hash_table[idx]

        # starting the next node as the first node is 0 and iterating to the last node
        while curr.next:
            # check for duplicates
            if curr.next.key == key:
                return
            curr = curr.next
        # adding the given key at the end
        curr.next = ListNode(key)

    def remove(self, key: int) -> None:
        idx = key % len(self.hash_table)
        curr = self.hash_table[idx]

        # starting the next node as the first node is 0 and iterating to the last node
        while curr.next:
            # if the key exists
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next

    def contains(self, key: int) -> bool:
        idx = key % len(self.hash_table)
        curr = self.hash_table[idx]

        # starting the next node as the first node is 0 and iterating to the last node
        while curr.next:
            # check for duplicates
            if curr.next.key == key:
                return True
            curr = curr.next
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
