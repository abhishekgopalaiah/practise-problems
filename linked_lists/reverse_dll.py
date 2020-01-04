"""
Reverse a doubly linked list
"""


def reverse(head):
    cur_node = head
    next_node = None

    while cur_node.next:
        next_node = cur_node.next
        cur_node.next = cur_node.prev
        cur_node.prev = next_node
        cur_node = next_node

    next_node = cur_node.next
    cur_node.next = cur_node.prev
    cur_node.prev = next_node

    head = cur_node
    return head
