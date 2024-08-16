# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_duplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    curr_node = head
    # return when the next pointer is null
    while curr_node and curr_node.next:
        if curr_node.val == curr_node.next.val:
            curr_node.next = curr_node.next.next
        else:
            curr_node = curr_node.next

    return head
