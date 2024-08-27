def get_intersection_node(head_a, head_b):
    left, right = head_a, head_b

    # keep iterating until they are the same
    while left != right:
        # if we reach at the end of any node, then we have to switch their starting positions
        left = left.next if left else head_b
        right = right.next if right else head_a

    # they both will appear at a common position if any or else None
    return left
