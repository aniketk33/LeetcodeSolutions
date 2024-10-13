from collections import OrderedDict


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        # for a doubly linked list
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        # store the key and nodes
        self.cache = {}
        # adding the dummy nodes to the left and right side
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        # making them point each other
        self.left.next = self.right
        self.right.prev = self.left

    # nodes are removed from the left side as they are the least recently used ones
    @staticmethod
    def remove_node(node):
        # get the left and right values for the given node
        left = node.prev
        right = node.next
        # break the connection
        left.next = right
        right.prev = left

    # these nodes are moved to the right side as they are most recently used
    def insert_node(self, node):
        left = self.right.prev
        right = self.right
        # make the new node connection
        node.prev = left
        node.next = right
        # update left node's connection
        left.next = node
        right.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            # remove the give node and move/insert it to the right side
            self.remove_node(self.cache[key])
            self.insert_node(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove_node(self.cache[key])
        # update or add the new node
        self.cache[key] = Node(key, value)
        # move/add to the right side
        self.insert_node(self.cache[key])

        # if current capacity is greater than remove the leftmost node
        if len(self.cache) > self.capacity:
            lru_node = self.left.next
            self.remove_node(lru_node)
            del self.cache[lru_node.key]


# using OrderedDict class
class LRUCache_2:
    def __init__(self, capacity):
        self.capacity = capacity
        # read more about OrderedDict
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.cache:
            # move the key to the end
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # move to the right side
            self.cache.move_to_end(key)
        # update or add the new node
        self.cache[key] = value

        # if current capacity is greater than remove the leftmost node
        if len(self.cache) > self.capacity:
            # pop the key from the left side
            self.cache.popitem(last=False)
