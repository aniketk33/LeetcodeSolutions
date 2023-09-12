"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_linked_list(nodes):
    left_ptr, right_ptr = None, nodes
    while right_ptr:
        temp = right_ptr.next
        right_ptr.next = left_ptr
        left_ptr = right_ptr
        right_ptr = temp
    return left_ptr


node_list = [1, 2, 3, 4, 5]  # create nodes using the class (haven't implemented)
# print(node_list)
# reverse_linked_list(node_list)
# print(node_list)
