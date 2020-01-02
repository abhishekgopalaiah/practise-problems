
class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None


def sortedInsert(head, data):
    node = DoublyLinkedListNode(data)
    if head is None:
        head = node
        return head
    temp = head
    while temp.data < node.data:

        if temp.next is None:
            temp.next = node
            node.prev = temp
            node.next = None
            temp = node
            return head

        temp = temp.next

    node.prev = temp.prev
    temp.prev = node
    node.next = temp

    if node.prev is not None:
        node.prev.next = node
    else:
        head = node
    return head