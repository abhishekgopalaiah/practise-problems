class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def append(head3,new_data):
    new_node = Node(new_data)
    if head3 is None: 
        head3 = new_node 
        return
    last = head3
    while (last.next): 
        last = last.next
    last.next =  new_node 


def mergeLists(head1, head2):
    head3 = Node(1)
    while head1 or head2:
        if head1 and head2:
            if head1.data <= head2.data:
                merge = head1
                head1 = head1.next
            else:
                merge = head2
                head2 = head2.next
        elif head1 is None:
            merge = head2
            head2 = head2.next
        elif head2 is None:
            merge = head1
            head1 = head1.next

        append(head3,merge.data)

    return head3.next
