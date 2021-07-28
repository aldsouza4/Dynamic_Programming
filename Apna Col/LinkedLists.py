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


def insertHead(root: Node, data):
    if root is None:
        return

    node = Node(data)
    node.next = root
    return node


def traverse(root: Node):
    if root is None or root.data is None:
        return

    current = root

    while current:
        print(current.data, end=" ")
        current = current.next


root = Node(1)
insertTail(root, 2)
insertTail(root, 3)
insertTail(root, 4)
insertTail(root, 5)
insertTail(root, 6)
root = insertHead(root, 0)
root = insertHead(root, -1)


def search(root: Node, data):
    if root is None:
        return False

    current = root

    while current:
        if current.data == data:
            return True
        current = current.next

    return False


def get_length(root: Node):
    if root is None:
        return 0

    count = 0
    current = root
    while current:
        current = current.next
        count += 1

    return count


def delete(root: Node, data):
    if root is None:
        return

    if root.data == data:
        temp = root.next
        del root
        return temp

    current = root

    while current.next:
        if current.next.data == data:
            if current.next.next:
                current.next = current.next.next

            else:
                current.next = None
            return root

        current = current.next

    print("Not Found")
    return


def reverse(root: Node):
    if root is None:
        return

    prev = None
    current = root

    while current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt

    return prev


def rotateK(root: Node, k):
    if root is None:
        return

    head = root
    current = root
    forward = root

    while k != 0 and forward.next:
        forward = forward.next
        k -= 1

    if forward.next is None:
        return

    while forward.next:
        current = current.next
        forward = forward.next

    newHead = current.next
    current.next = None

    while newHead.next:
        newHead = newHead.next

    newHead.next = head
    return newHead


# root = rotateK(root, 1)
# traverse(root)


def detectCycle(root: Node):
    if root is None:
        return False

    slow = root
    fast = root

    while fast and fast.next.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return slow

    return False


def removeCycle(root: Node):
    if root is None:
        return

    inpointer = detectCycle(root)

    if not inpointer:
        print("No cycle found")
        return

    head = root

    while True:
        if head.next == inpointer.next:
            inpointer.next = None
            return root

        head = head.next
        inpointer = inpointer.next


# root = Node(1)
# root.next = Node(2)
# root.next.next = Node(3)
# root.next.next.next = Node(4)
# root.next.next.next.next = Node(5)
# root.next.next.next.next.next = Node(6)
# root.next.next.next.next.next.next = root.next.next
root = removeCycle(root)
traverse(root)


def reverseknodes(root: Node, k):
    if root is None:
        return

    prev = None
    current = root
    count = 0
    nxt = None

    while current is not None and count < k:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
        count += 1

    if nxt:
        root.next = reverseknodes(nxt, k)

    return prev


# root = reverseknodes(root, 2)
# traverse(root)

# using no extra space
def findmergepoint(root1: Node, root2: Node):
    if not root1 or not root2:
        return

    l1 = get_length(root1)
    l2 = get_length(root2)

    current1 = root1
    current2 = root2

    if l1 > l2:
        i1 = l1 - l2

        while i1:
            current1 = current1.next
            i1 -= 1

    elif l2 > l1:
        i2 = l2 - l1

        while i2:
            current2 = current2.next
            i2 -= 1

    while current1 and current2:
        if current1 == current2:
            return current1

        current1 = current1.next
        current2 = current2.next

    return


# merge two sorted linked lists in a sorted manner
def mergells(root1: Node, root2: Node):
    if root1 is None:
        return root2

    if root2 is None:
        return root1

    if root1.data <= root2.data:
        r = Node(root1.data)
        r.next = mergells(root1.next, root2)

    if root2.data < root1.data:
        r = Node(root2.data)
        r.next = mergells(root1, root2.next)

    return r


# root = mergells(root, root2)
# traverse(root)


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

# root = oddEven(root)
# traverse(root)
