"""
Reverse a linked list
"""


def reverse(head):
    prev = None
    cur_node = head

    while cur_node:
        next_node = cur_node.next
        cur_node.next = prev
        prev = cur_node
        cur_node = next_node

    head = prev
    return head
