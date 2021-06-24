from collections import deque


class Node:

    # Constructor to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# A utility function to do inorder traversal of BST
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key)
        inorder(root.right)


# A utility function to insert a
# new node with given key in BST
def insert(node: Node, key):
    # If the tree is empty, return a new node
    if node is None:
        return Node(key)

    # Otherwise recur down the tree
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    # return the (unchanged) node pointer
    return node


# Given a non-empty binary
# search tree, return the node
# with minum key value
# found in that tree. Note that the
# entire tree does not need to be searched


def minValueNode(node):
    current = node

    # loop down to find the leftmost leaf
    while current.left is not None:
        current = current.left

    return current


# Given a binary search tree and a key, this function
# delete the key and returns the new root
def search(root, key):
    # Base Cases: root is null or key is present at root
    if root is None or root.val == key:
        return root

    # Key is greater than root's key
    if root.val < key:
        return search(root.right, key)

    # Key is smaller than root's key
    return search(root.left, key)


def deleteNode(root, key):
    # Base Case
    if root is None:
        return root

    # If the key to be deleted
    # is smaller than the root's
    # key then it lies in left subtree
    if key < root.key:
        root.left = deleteNode(root.left, key)

    # If the kye to be delete
    # is greater than the root's key
    # then it lies in right subtree
    elif key > root.key:
        root.right = deleteNode(root.right, key)

    # If key is same as root's key, then this is the node
    # to be deleted
    else:

        # Node with only one child or no child
        if root.left is None:
            temp = root.right
            del root
            return temp

        elif root.right is None:
            temp = root.left
            del root
            return temp

        # Node with two children:
        # Get the inorder successor
        # (smallest in the right subtree)
        temp = minValueNode(root.right)

        # Copy the inorder successor's
        # content to this node
        root.key = temp.key

        # Delete the inorder successor
        root.right = deleteNode(root.right, temp.key)

    return root


# Constructing a binary search tree from given preorder sequence
def constructBST(preorder, key, min, max, n):
    global preindex
    root = None

    if preindex >= n:
        return root

    if min < key < max:
        root = Node(key)

        preindex += 1

        if preindex < n:
            root.left = constructBST(preorder, preorder[preindex], min, key, n)

        if preindex < n:
            root.right = constructBST(preorder, preorder[preindex], key, max, n)

    return root


# preoreder = [5, 4, 2, 3, 8, 6, 9]
# preindex = 0
# root = constructBST(preoreder, preoreder[0], -float('inf'), float('inf'), len(preoreder))
# inorder(root)

# Check if a given binary tree is a binary search tree or not
def checkBST(root: Node, min, max):
    if root is None:
        return True


    left = checkBST(root.left, min, root.key)
    right = checkBST(root.right, root.key, max)

    if min < root.key < max:
        if left and right:
            return True

    return False


# print(checkBST(head, -float('inf'), float('inf')))


# Build a balanced binary search tree using a sorted array
def buildbst(arr, start, end):
    if start > end:
        return

    mid = (start + end)//2

    root = Node(arr[mid])

    root.left = buildbst(arr, start, mid-1)
    root.right = buildbst(arr, mid + 1, end)

    return root


# root = buildbst([1, 2, 3, 4, 5, 6, 7], 0, 6)
# preorder(root)


# Print nth catalan number
def catalan(n):
    global memo
    if n in memo:
        return memo[n]

    if n <= 1:
        return 1

    res = 0
    for i in range(n):
        temp = catalan(i)
        memo[i] = temp

        temp = catalan(n - i - 1)
        memo[n - i - 1] = temp

        res += memo[i] * memo[n - i - 1]

    memo[n] = res
    return memo[n]


# Function to return the count of unique BSTs with n keys
def uniqueBSTs(n):
    n1, n2, sum = 0, 0, 0

    # Base cases
    if n == 1 or n == 0:
        return 1

    # Find the nth Catalan number
    for i in range(1, n + 1):
        # Recursive calls
        n1 = uniqueBSTs(i - 1)
        n2 = uniqueBSTs(n - i)
        sum += n1 * n2

    # Return the nth Catalan number
    return sum


# Prints the level order in a zigzag way
def zigzagtraversal(root: Node):
    if root is None:
        return

    queue = deque([root])
    left = True
    ans = []
    while queue:

        count = len(queue)
        oparr = []
        while count:
            curr = queue.popleft()

            if curr.left:
                queue.append(curr.left)

            if curr.right:
                queue.append(curr.right)

            oparr.append(curr.key)
            count -= 1

        if left:
            ans += oparr
        else:
            ans += oparr[::-1]

        left = not left

    return ans


# print(zigzagtraversal(head))


# Check if two binary trees are identical or not
def identicalBST(root1: Node, root2: Node):
    if root1 is None and root2 is None:
        return True

    if root1 is None or root2 is None:
        return False

    left = identicalBST(root1.left, root2.left)
    right = identicalBST(root1.right, root2.right)

    if root1.key == root2.key:
        return left and right

    return False


# To find the largest binary search tree in a binary tree
class Info:
    def __init__(self):
        self.size = None
        self.max = None
        self.min = None
        self.ans = None
        self.isBST = None


def largestBSTinBT(root: Node):
    if root is None:
        temp = Info()
        temp.size = 0
        temp.max = -float('inf')
        temp.min = float('inf')
        temp.ans = 0
        temp.isBST = True
        return temp

    if root.left is None and root.right is None:
        temp = Info()
        temp.size = 1
        temp.max = root.key
        temp.min = root.key
        temp.ans = 1
        temp.isBST = True
        return temp

    leftInfo = largestBSTinBT(root.left)
    rightInfo = largestBSTinBT(root.right)

    curr = Info()
    curr.size = 1 + leftInfo.size + leftInfo.size

    if leftInfo.isBST and rightInfo.isBST and leftInfo.max < root.key < rightInfo.min:
        curr.min = min(leftInfo.min, rightInfo.min, root.key)
        curr.max = max(rightInfo.max, leftInfo.max, root.key)

        curr.ans = curr.size
        curr.isBST = True

        return curr

    else:
        curr.ans = max(leftInfo.ans, rightInfo.ans)
        curr.isBST = False
        return curr
    # returns an Info class object (.ans for final ans)


# Recover binary tree
def calcpointers(root):
    global first, mid, last, prev
    if root is None:
        return

    calcpointers(root.left)

    if prev and root.key < prev.key:
        if not first:
            first = prev
            mid = root

        else:
            last = root

    prev = root

    calcpointers(root.right)


def swap(node1, node2):
    node1.key, node2.key = node2.key, node1.key


first = None
mid = None
last = None
prev = None


def restoreBST(root: Node):
    global first, mid, last, prev
    calcpointers(root)
    if first and last:
        swap(first, last)

    else:
        swap(first.key, mid.key)


# Driver code
""" 
        Let us create following BST
		   50
		 /	  \
		30	  70
		/ \   / \
	   20 40 60 80 	   
"""

root = Node(50)
insert(root, 30)
insert(root, 20)
insert(root, 40)
insert(root, 70)
insert(root, 60)
insert(root, 80)
