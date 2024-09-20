def rotate_list(head, k):
    if not head:
        return None
    # reach the end make the node circular. also, count the total length
    last_node = head
    count = 1

    while last_node.next:
        last_node = last_node.next
        count += 1

    # this gives the starting index of the first node after rotation
    k = k % count
    # return if no rotation is required
    if k == 0:
        return head

    # making it circular
    last_node.next = head

    # move until the starting position
    temp = head
    for _ in range(count - k - 1):
        temp = temp.next

    # this is the starting point of the rotated list
    # for e.g. [1,2,3,4,5], after 2 rotations it will be [4,5,1,2,3]
    final_node = temp.next
    # break the link after reaching the starting point
    temp.next = None

    return final_node
