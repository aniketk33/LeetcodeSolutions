"""You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_lists(l1, l2):
    left_ptr = ListNode()
    result = left_ptr
    while l1 and l2:
        if l1.val < l2.val:
            result.next = l1
            l1 = l1.next
        else:
            result.next = l2
            l2 = l2.next
        result = result.next

    if l1:
        result.next = l1
    if l2:
        result.next = l2

    return left_ptr.next
