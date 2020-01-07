"""
Level order traversal of a tree is breadth first traversal for the tree.
printLevelorder(tree)
1) Create an empty queue q
2) temp_node = root /*start from root*/
3) Loop while temp_node is not NULL
a) print temp_node->data.
b) Enqueue temp_node’s children (first left then right children) to q
c) Dequeue a node from q and assign it’s value to temp_node
"""
def levelOrder(root):
    q = []
    temp_node = root
    while temp_node:
        print(temp_node.info, end=' ')
        if temp_node.left:
            q.append(temp_node.left)
        if temp_node.right:
            q.append(temp_node.right)
        if len(q) > 0:
            temp_node = q.pop(0)
        else:
            return


