class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_duplicates(head: ListNode):
    # initialize an empty node
    left_ptr = ListNode()
    right_ptr = head
    temp = left_ptr
    duplicates = set()

    while right_ptr and right_ptr.next:
        if right_ptr.val == right_ptr.next.val:
            # go to a unique node
            duplicates.add(right_ptr.val)
            while right_ptr and right_ptr.val in duplicates:
                right_ptr = right_ptr.next
            # if the last node is a duplicate node, we need to set the last unique node to None
            if not right_ptr and temp.next and temp.next.val in duplicates:
                temp.next = None
        else:
            temp.next = right_ptr
            temp = temp.next
            right_ptr = right_ptr.next

    # for the last node
    while right_ptr:
        temp.next = right_ptr
        temp = left_ptr.next
        right_ptr = right_ptr.next

    return left_ptr.next
