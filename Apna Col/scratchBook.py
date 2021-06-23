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


# Driver code
""" Let us create following BST
		   50
		 /	  \
		30	  70
		/ \   / \
	   20 40 60 80 """

head = Node(50)
insert(head, 30)
insert(head, 20)
insert(head, 40)
insert(head, 70)
insert(head, 60)
insert(head, 80)



