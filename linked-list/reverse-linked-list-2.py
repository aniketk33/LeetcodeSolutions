class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head: ListNode, left, right):
    # base condition
    if not head or left == right:
        return head

    dummy = ListNode(next=head)

    left_prev = dummy
    curr = head

    # get the left position node iterating left-1 times
    for _ in range(left - 1):
        left_prev = left_prev.next
        curr = curr.next

    # reverse the list right-left+1 times using a prev node which is None initially
    prev = None
    for _ in range(right - left + 1):
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    # after getting all the required nodes, make the connection
    left_prev.next.next = curr
    left_prev.next = prev

    return dummy.next
