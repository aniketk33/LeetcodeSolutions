# optimal solution with time O(n) and space O(1)
def is_linked_list_palindrome(head):
    def reverse(mid_node):
        prev = None
        curr = mid_node

        while curr:
            # store the current's next node (storing current's next node temporarily)
            next_temp = curr.next
            # make a connection to the previous node
            curr.next = prev
            # move the previous node to the current node
            prev = curr
            # move the current node to the next node where we stored temporarily
            curr = next_temp

        return prev

    slow, fast = head, head

    # when the fast's next is None, then current is the middle node
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # reverse starting from the middle
    reversed_node = reverse(slow)

    while reversed_node:
        if head.val != reversed_node.val:
            return False

        head = head.next
        reversed_node = reversed_node.next

    return True


# less optimal with time O(n) and space O(n)
def is_linked_list_palindrome_2(head):
    node_arr = []
    # move the nodes to an array
    while head:
        node_arr.append(head.val)
        head = head.next

    # apply the palindrome approach to an array
    left, right = 0, len(node_arr) - 1

    while left <= right:
        if node_arr[left] != node_arr[right]:
            return False
        left += 1
        right -= 1

    return True
