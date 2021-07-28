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

root1 = Node(3)
# root1.left = Node(6)
# root1.right = Node(7)


def isSubTree(main, sub):
    if sub is None:
        return True

    if main is None:
        return False

    def inorder(root: Node, ans: list):
        if root is None:
            return

        inorder(root.left, ans)
        ans.append(root.data)
        inorder(root.right, ans)

    def preorder(root: Node, ans: list):
        if root is None:
            return

        ans.append(root.data)
        preorder(root.left, ans)
        preorder(root.right, ans)

    main_inorder = []
    sub_inorder = []
    inorder(root, main_inorder)
    inorder(sub, sub_inorder)

    main_inorder = "".join([str(i) for i in main_inorder])
    sub_inorder = "".join([str(i) for i in sub_inorder])

    main_preorder = []
    sub_preorder = []
    preorder(root, main_preorder)
    preorder(sub, sub_preorder)

    main_preorder = "".join([str(i) for i in main_preorder])
    sub_preorder = "".join([str(i) for i in sub_preorder])

    if sub_inorder in main_inorder:
        if sub_preorder in main_preorder:
            return True

    return False


print(isSubTree(root, root1))
