class ListNode:
    def __init__(self, key=-1, value=-1, next=None):
        self.key = key
        self.val = value
        self.next = next


class MyHashMap:

    def __init__(self):
        # storing the key and value for the particular index
        self.hash_table = [ListNode() for _ in range(10 ** 4)]

    def put(self, key: int, value: int) -> None:
        idx = key % len(self.hash_table)
        curr = self.hash_table[idx]

        # starting the next node as the first node is 0 and iterating to the last node
        while curr.next:
            # if exists
            if curr.next.key == key:
                # update its value
                curr.next.val = value
                return
            curr = curr.next
        # adding the given key at the end
        curr.next = ListNode(key, value)

    def get(self, key: int) -> int:
        idx = key % len(self.hash_table)
        curr = self.hash_table[idx]

        # starting the next node as the first node is 0 and iterating to the last node
        while curr.next:
            # check for duplicates
            if curr.next.key == key:
                return curr.next.val
            curr = curr.next
        return -1

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

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
