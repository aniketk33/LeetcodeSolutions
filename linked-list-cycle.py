class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def is_circular(head: ListNode):
    # check for single item
    if not head.next:
        return False
    # a slow pointer takes only one step and a fast pointer takes two steps
    # and if they meet at a certain point then there is a cycle in the list
    slow_ptr, fast_ptr = head, head
    while fast_ptr and fast_ptr.next:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next

        if slow_ptr == fast_ptr:
            return True

    return False
