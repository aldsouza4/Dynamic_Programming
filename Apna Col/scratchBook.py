class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def traverse(root: Node):
    if root is None:
        return

    traverse(root.left)
    print(root.data)
    traverse(root.right)


root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.right = Node(3)
root.right.left = Node(6)
root.right.right = Node(7)

from collections import deque


