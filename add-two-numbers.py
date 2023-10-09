# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""For better understanding refer FREEFORM"""


def add_two_numbers(l1: ListNode, l2: ListNode):
    result_node = ListNode()
    current_node = result_node
    carry = 0
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        # get the addition
        num_sum = val1 + val2 + carry
        # store the carry
        carry = num_sum // 10
        # get the remainder and create a node
        num_sum = num_sum % 10
        current_node.next = ListNode(num_sum)
        # update pointers
        current_node = current_node.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return result_node.next
