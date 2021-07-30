class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.nextRight = None


def traverse(root: Node):
    if root is None:
        return

    print(root.data)
    traverse(root.left)
    traverse(root.right)


# root = Node(22)
# root.left = Node(9)
# root.left.left = Node(4)
# root.left.right = Node(5)
# root.right = Node(13)
# root.right.left = Node(6)
# root.right.right = Node(7)


root = Node(62)
root.left = Node(16)
root.right = Node(15)
root.left.right = Node(8)
root.left.right.right = Node(8)
root.right.left = Node(4)
root.right.right = Node(7)
root.right.left.left = Node(4)


class Solution:
    def __init__(self):
        self.condition = True

    def isSumTree(self, root: Node):
        self.SumTree(root)
        return self.condition

    def SumTree(self, root: Node):
        if root is None:
            return 0
        k = root.data

        if root.left is None and root.right is None:
            return root.data

        left = self.SumTree(root.left)
        right = self.SumTree(root.right)

        if left + right != root.data:
            self.condition = False

        return left + right + root.data


x = Solution()
# print(x.isSumTree(root))
