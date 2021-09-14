class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def traverse(head: Node):
    if head is None:
        return

    print(head.data)
    traverse(head.next)


s = Node(1)
s.next = Node(2)
s.next.next = Node(3)
s.next.next.next = Node(4)
s.next.next.next.next = Node(5)

k = Node(2)
k.next = Node(4)
k.next.next = Node(5)
k.next.next.next = Node(7)
k.next.next.next.next = Node(9)



