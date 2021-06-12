from DP_Trees import Node, BinarySearchTree
root = Node(6)
root.right = Node(5)
root.right.right =Node(4)
root.left = Node(3)
root.left.left = Node(2)
root.left.right = Node(5)
root.left.right.left = Node(7)
root.left.right.right = Node(4)

# root2 = Node(5)
# root2.left = Node(3)
# root2.left.right = Node(4)
# root2.left.left = Node(2)
# root2.right = Node(7)
# root2.right.left = Node(6)
# root2.right.right = Node(8)
#
#
# root1 = Node(10)
# root1.left = Node(10)
# root1.left.right = Node(8)
# root1.left.left = Node(3)
# root1.right = Node(15)
# root1.right.left = Node(11)
# root1.right.right = Node(18)


# root = Node(2)
# root.right = Node(5)
# root.right.right = Node(1)
# root.left = Node(7)
# root.left.right = Node(9)
# root.left.right.left = Node(11)
# root.left.right.right = Node(4)

# root = Node(2)
# root.left = Node(3)
# root.right = Node(4)

global k
k = 3
def findkthele(root: Node):
    global k

    if root is None:
        return

    left = findkthele(root.left)

    if left is not None:
        return left

    k -= 1

    if k == 0:
        return root.data

    return findkthele(root.right)


print(findkthele(root))











