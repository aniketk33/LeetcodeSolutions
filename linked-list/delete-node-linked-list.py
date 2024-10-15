def delete(node):
    # get the next node's value and next next pointer
    val = node.next.val
    next_node = node.next.next

    # assign it to itself and skip the next connection
    node.val = val
    node.next = next_node
