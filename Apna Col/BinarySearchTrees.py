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


preoreder = [5, 4, 2, 3, 8, 6, 9]
preindex = 0
# root = constructBST(preoreder, preoreder[0], -float('inf'), float('inf'), len(preoreder))
# inorder(root)

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
