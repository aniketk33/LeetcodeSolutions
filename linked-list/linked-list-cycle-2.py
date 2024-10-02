# constant space solution
def cycle(head):
    slow = fast = head

    # using slow and fast pointer approach, detect the cycle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    # if cycle not found
    else:
        return None

    # after detecting, reset the slow pointer and move both the pointers at the same speed
    slow = head
    # their next meeting point will be the start node of the cycle
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow


# extra space solution
def cycle_2(head):
    visited = set()

    while head:
        if head in visited:
            return head
        visited.add(head)
        head = head.next

    return None
