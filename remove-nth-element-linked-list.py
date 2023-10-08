# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""Check FREEFORM for better understanding"""


def remove_nth_from_end(head: ListNode, n):
    dummy_node = ListNode(0, next=head)
    left_ptr, right_ptr = dummy_node, head
    # setting the right pointer to head + n
    while n > 0:
        right_ptr = right_ptr.next
        n -= 1

    while right_ptr:
        left_ptr = left_ptr.next
        right_ptr = right_ptr.next

    # delete the nth element
    left_ptr.next = left_ptr.next.next

    return dummy_node.next
