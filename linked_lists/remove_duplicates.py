def removeDuplicates(head):
    if head is None:
        return head
    cur = head
    while cur.next:
        if cur.data == cur.next.data:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return head