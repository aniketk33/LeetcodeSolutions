# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


"""Check FREEFORM for better understanding"""


def copy_random(head: Node):
    deep_copy = {
        None: None
    }

    # creating empty nodes
    current = head
    while current:
        copy = Node(current.val)
        deep_copy[current] = copy
        current = current.next

    # linking old nodes to newly created deep copy
    current = head
    while current:
        copy = deep_copy[current]
        copy.next = deep_copy[current.next]
        copy.random = deep_copy[current.random]
        current = current.next

    return deep_copy[head]
