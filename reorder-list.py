"""For better visual understanding go to FREEFORM"""


def reorder_list(head):
    slow_ptr, fast_ptr = head, head.next
    while fast_ptr and fast_ptr.next:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next

    # reversing the second half
    second_list_start_element = slow_ptr.next
    prev_element = slow_ptr.next = None
    while second_list_start_element:
        next_element = second_list_start_element.next
        # breaking the chain
        second_list_start_element.next = prev_element
        # moving the prev_element pointer to current position
        prev_element = second_list_start_element
        second_list_start_element = next_element

    # merging the two halves
    first, second = head, prev_element
    while second:
        temp1, temp2 = first.next, second.next
        first.next = second
        second.next = temp1
        first, second = temp1, temp2
