class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def insertTail(root: Node, data):
    if root is None or root.data is None:
        return Node(data)

    current = root

    while current.next:
        current = current.next

    current.next = Node(data)


def get_length(root: Node):
    if root is None:
        return 0

    count = 0
    current = root
    while current:
        current = current.next
        count += 1

    return count


def traverse(root: Node):
    if root is None or root.data is None:
        return

    current = root

    while current:
        print(current.data, end=" ")
        current = current.next


# Using O(N) Extra space
def mergepoint(root1: Node, root2: Node):
    if not root1 or not root2:
        return

    map = set()

    current = root1

    while current:
        map.add(current)
        current = current.next

    current = root2
    while current:
        if current in map:
            return current.data

        current = current.next

    print("No merge point")
    return


# print(mergepoint(root, root2))


root = Node(1)
root.next = Node(2)
root.next.next = Node(3)
root.next.next.next = Node(4)
root.next.next.next.next = Node(5)
root.next.next.next.next.next = Node(6)
root.next.next.next.next.next.next = Node(7)
root.next.next.next.next.next.next.next = Node(8)
root.next.next.next.next.next.next.next.next = Node(9)
root.next.next.next.next.next.next.next.next.next = Node(10)
root.next.next.next.next.next.next.next.next.next.next = Node(11)


# collect all odd position nodes first and then the even position nodes
def oddEven(root: Node):
    if root is None:
        return

    odd = root
    even = root.next

    evenFirst = even

    while True:
        if odd is None or even is None or even.next is None:
            odd.next = evenFirst
            break

        odd.next = even.next
        odd = odd.next

        if odd.next is None:
            even.next = None
            odd.next = evenFirst
            break

        even.next = odd.next
        even = even.next

    return root


root = oddEven(root)
traverse(root)