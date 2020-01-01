

def find_merge_node(head1, head2):
    cur1 = head1
    cur2 = head2
    while not cur1 == cur2:
        if cur1.next is None:
            cur1 = head2
        else:
            cur1 = cur1.next
        if cur2.next is None:
            cur2 = head1
        else:
            cur2 = cur2.next
    return cur1.data

