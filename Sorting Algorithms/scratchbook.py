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


# root = Node(4)
# root.left = Node(2)
# root.left.left = Node(1)
# root.left.right = Node(3)
# root.right = Node(6)
# root.right.left = Node(-5)
# root.right.right = Node(-7)

# root = Node(-9)
# root.left = Node(6)
# root.right = Node(-10)


root = Node(1)
root.left = Node(8)
root.right = Node(6)
root.left.left = Node(-7)
root.left.right = Node(-10)
root.right.left = Node(-9)


class Info:
    def __init__(self, min=-float('inf'), max=float('inf'), ans=0, size=0, isBst=False):
        self.min = min
        self.max = max
        self.ans = ans
        self.size = size
        self.isBst = isBst


# To check for the larget binary searh Tree in a Binary Tree
def bstinbt(root: Node):
    if root is None:
        return Info()

    if root.left is None and root.right is None:
        return Info(root.data, root.data, 1, 1, True)

    leftbst = bstinbt(root.left)
    rightbst = bstinbt(root.right)

    curr = Info()
    curr.size = leftbst.size + rightbst.size + 1

    if leftbst.isBst and rightbst.isBst and rightbst.min > root.data > leftbst.max:
        curr.min = min(rightbst.min, leftbst.min, root.data)
        curr.max = max(rightbst.min, leftbst.min, root.data)
        curr.ans = curr.size
        curr.isBst = True

    else:
        curr.ans = max(leftbst.ans, rightbst.ans)
        curr.isBst = False

    return curr


