from DP_Trees import Node, BinarySearchTree
root = Node(6)

t = BinarySearchTree()
t.root = root

root.right = Node(5)
root.right.right =Node(4)
root.left = Node(3)
root.left.left = Node(2)
root.left.right = Node(5)
root.right.left = Node(4)
root.right.left.right = Node(4)

# root = Node(1)
# root.right = Node(2)
# root.right.right = Node(8)
# root.left = Node(3)
# root.left.left = Node(4)
# root.left.left.left = Node(4)

def checkcomplete(root: Node):
    if root is None:
        return True

    if not root.left and root.right:
        return False

    if not root.right and root.left:
        return False

    if not root.left and not root.right:
        return True

    left = checkcomplete(root.left)
    right = checkcomplete(root.right)

    if left is False or right is False:
        return False

    return True


t.traverse_in_order(t.root)






