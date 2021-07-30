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


class Solution:
    def verticalTraversal(self, root):
        res = []
        dictionary = dict()

        def function(root, vertical=0, horizontal=0):
            if not root:
                return

            if vertical in dictionary:
                dictionary[vertical].append((horizontal, root.data))
            else:
                dictionary[vertical] = [(horizontal, root.data)]

            function(root.left, vertical - 1, horizontal + 1)
            function(root.right, vertical + 1, horizontal + 1)

        function(root)

        # structure of dictionary = {index:[(level, value)]}

        for i in sorted(dictionary.keys()):  # Sorting the keys(indices)
            temp = [j[1] for j in sorted(dictionary[i])]  # Sorting in case of a tie
            res.append(temp)
        
        ans = []
        for i in res:
            for j in i:
                ans.append(j)

        return res


x = Solution
print(x.verticalTraversal(x, root))