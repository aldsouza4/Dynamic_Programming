from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def traverse(node: Node):
    if node is None:
        return
    traverse(node.left)
    print(node.data)
    traverse(node.right)
    return


root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.right = Node(3)
root.right.left = Node(6)
root.right.right = Node(7)

# Construct Tree from given Inorder and Preorder traversals

preIndex = 0


def search(inorder, start, end, val):
    for i in range(start, end + 1):
        if inorder[i] == val:
            return i


def buildTree(inOrder, preorder, instart, inend):
    global preIndex

    if instart > inend:
        return

    tNode = Node(preorder[preIndex])
    preIndex += 1

    if instart == inend:
        return tNode

    inIndex = search(inOrder, instart, inend, tNode.data)

    tNode.left = buildTree(inOrder, preorder, instart, inIndex - 1)
    tNode.right = buildTree(inOrder, preorder, inIndex + 1, inend)

    return tNode


poIndex = 0


# Build Tree Postorder and Inorder
def Build_IN_POST(inorder, postorder):
    global poIndex
    poIndex = len(inorder) - 1

    def buildTreePostInor(inOrder, postrder, instart, inend):
        global poIndex

        if instart > inend:
            return

        tNode = Node(postrder[poIndex])
        poIndex -= 1

        if instart == inend:
            return tNode

        inIndex = search(inOrder, instart, inend, tNode.data)

        tNode.right = buildTreePostInor(inOrder, postrder, inIndex + 1, inend)
        tNode.left = buildTreePostInor(inOrder, postrder, instart, inIndex - 1)

        return tNode

    return buildTreePostInor(inorder, postorder, 0, len(inorder) - 1)


def countNodes(node: Node):
    if node is None:
        return 0

    left = countNodes(node.left)
    right = countNodes(node.right)

    return 1 + left + right


def sumnodes(node: Node):
    if node is None:
        return 0

    left = sumnodes(node.left)
    right = sumnodes(node.right)

    return node.data + left + right


# print(sumnodes(root))

# convert a Binary Tree to a linked list in preorder traversal
def converttoList(root: Node):
    if root is None or (root.left is None and root.right is None):
        return

    if root.left is not None:
        converttoList(root.right)

        temp = root.right
        root.right = root.left
        root.left = None

        curr = root.right
        while curr.right:
            curr = curr.right

        curr.right = temp

    converttoList(root.right)


# height of a binary tree
def height(root: Node):
    if root is None:
        return -1

    left = height(root.left)
    right = height(root.right)

    return 1 + max(left, right)


ans = 0


def diameter(root: Node):
    global ans

    if root is None:
        return 0

    left = diameter(root.left)
    right = diameter(root.right)

    temp = 1 + max(left, right)
    ans = max(1 + left + right, ans)

    return temp


# the answer will be stored in the ans variable


max_level = 0


# Print leftView of a Tree
def leftview(root: Node, curr_level=0):
    global max_level
    if root is None:
        return

    elif curr_level == max_level:
        print(root.data)
        max_level += 1

    leftview(root.left, curr_level + 1)
    leftview(root.right, curr_level + 1)


# Print rightView of a Tree
def rightview(root: Node, curr_level=0):
    global max_level
    if root is None:
        return

    elif curr_level == max_level:
        print(root.data)
        max_level += 1

    rightview(root.right, curr_level + 1)
    rightview(root.left, curr_level + 1)


# O(n^2)
# Function to check if tree is balanced or not
def isbalanced(node: Node):
    if node is None:
        return True

    if isbalanced(node.left) is False:
        return False

    elif isbalanced(node.right) is False:
        return False

    left = height(node.left)
    right = height(node.right)

    if abs(left - right) <= 1:
        return True

    else:
        return False


# O(n)
def isBalanced(root):
    if root is None:
        # returning height=0 for leaf nodes.
        return 0
    lh = isBalanced(root.left)
    rh = isBalanced(root.right)
    # checking if the subtree is ever false then returning
    # false for the whole recursion
    if lh is False or rh is False:
        return False
    if abs(lh - rh) > 1:
        # returning false if subtree is not balanced
        return False
    else:
        # returning height if subtree is balanced
        return max(lh, rh) + 1


# Traverse a Tree level by level
def travlevel(node: Node):
    if node is None:
        return

    queue = deque([node])

    while queue:

        count = len(queue)

        while count:
            curr = queue.popleft()
            print(curr.data, end=" ")

            if curr.left:
                queue.append(curr.left)

            if curr.right:
                queue.append(curr.right)

            count -= 1

        print("")


# Sum at k level in Binary Tree
def sumatk(node: Node, k: int):
    if node is None:
        return

    queue = deque([node])

    while queue:

        count = len(queue)
        k -= 1

        if k == 0:
            return sum([x.data for x in queue])

        while count:
            if k != 0:
                curr = queue.popleft()

                if curr.left:
                    queue.append(curr.left)

                if curr.right:
                    queue.append(curr.right)

            count -= 1


# Print path from root to key
path = []


def getpath(root: Node, key: int, path: list):
    if root is None:
        return False

    path.append(root.data)

    if root.data == key:
        return True

    if getpath(root.left, key, path) or getpath(root.right, key, path):
        return True

    path.pop()
    return False


#   Ans is stored in path

# getpath(root, 7, path)
# print(path)


# Lowest common ancestor between two nodes
def lowestansesotor(root: Node, v1: int, v2: int):
    if root is None:
        return

    path1 = []
    path2 = []

    if not getpath(root, v1, path1) or not getpath(root, v2, path2):
        return False

    index = 0
    while index < min(len(path1), len(path2)):
        if path1[index] != path2[index]:
            break
        index += 1

    return path1[index - 1]


# print(lowestansesotor(root, 7, 6))

root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.right = Node(3)
root.right.left = Node(6)
root.right.right = Node(7)


# Lowest common ancestor between two nodes (Single Pass)
def leastancestor(root: Node, n1, n2):
    if root is None:
        return

    if root.data == n1 or root.data == n2:
        return root

    leftlca = leastancestor(root.left, n1, n2)
    rightlca = leastancestor(root.right, n1, n2)

    if leftlca and rightlca:
        return root

    if leftlca is not None:
        return leftlca

    if rightlca is not None:
        return rightlca


#     Returns common ancestor node... so we have to return node.data

print(leastancestor(root, 4, 5).data)

# Get the path with highest sum
result = -float('inf')


def max_sum_path(self):
    global result

    def maxpath(node: Node):
        global result
        if node is None:
            return 0

        left = maxpath(node.left)
        right = maxpath(node.right)

        temp = max(max(left, right) + node.data, node.data)
        ans = max(left + right + node.data, temp)
        result = max(ans, self.result)
        return temp

    maxpath(root)
    return result


# Print Nodes at distance kfrom thr root node
def distancek(root: Node, k):
    if root is None:
        return

    if k == 0:
        print(root.data)
        return

    distancek(root.left, k - 1)
    distancek(root.right, k - 1)


# Prints all nodes at distnace from given key/target
def alldistnacek(root: Node, key, k):
    if root is None:
        return -1

    if key == root.data:
        distancek(root, k)
        return 0

    dl = alldistnacek(root.left, key, k)

    if dl != -1:

        if dl + 1 == k:
            print(root.data)

        else:
            distancek(root.right, k - dl - 2)

        return dl + 1

    dr = alldistnacek(root.right, key, k)

    if dr != -1:

        if dr + 1 == k:
            print(root.data)

        else:
            distancek(root.left, k - dr - 2)

        return dr + 1

    return -1


# alldistnacek(root, 2, 1)


# Returns the minimum distance between two nodes in a Tree (Requires get path function).
def getcomancestor(root: Node, n1, n2):
    if root is None:
        return

    path1 = []
    path2 = []

    getpath(root, n1, path1)
    getpath(root, n2, path2)

    i = 0
    while True:
        if path1[i] != path2[i]:
            break
        i += 1

    return len(path1[i:]) + len(path2[i:])


# print(getcomancestor(root, 4, 3))


# Replace every node in the tree with sum of left and sum of right chilren
def sumreplacement(root: Node):
    if root is None:
        return 0

    left = sumreplacement(root.left)
    right = sumreplacement(root.right)

    root.data = root.data + left + right
    return root.data


# sumreplacement(root)


# Print vaerical order of teh tree


def verticalTraversal(root):
    res = []
    dictionary = dict()

    def function(root, vertical, horizontal):
        if not root:
            return

        if vertical in dictionary:
            dictionary[vertical].append((horizontal, root.data))
        else:
            dictionary[vertical] = [(horizontal, root.data)]
        function(root.left, vertical - 1, horizontal + 1)
        function(root.right, vertical + 1, horizontal + 1)

    function(root, 0, 0)
    # structure of dictionary = {index:[(level, value)]}
    # print(dictionary)
    for i in sorted(dictionary.keys()):  # Sorting the keys(indices):
        temp = [j[1] for j in sorted(dictionary[i])]  # Sorting in case of a tie
        res.append(temp)

    return res


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


root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(6)
root.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)
