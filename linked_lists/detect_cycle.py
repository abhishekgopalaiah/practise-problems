"""
Sample Input

The following linked lists are passed as arguments to your function:

Sample Inputs
Sample Output

0
1
Explanation

The first list has no cycle, so we return false and the hidden code checker prints  to stdout.
The second list has a cycle, so we return true and the hidden code checker prints  to stdout.
"""
def has_cycle(head):
    slow = head
    fast = head
    if not head:
        return 0
    while slow and fast:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return 1