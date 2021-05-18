# Node class
class Node:

    # Function to initialize the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize
    # next as null


# Linked List class
class LinkedList:

    # Function to initialize the Linked
    # List object
    def __init__(self):
        self.head = None

    def insert(self, data):
        if self.head is None:
            self.head = Node(data)

        else:
            current = self.head

            while current.next:
                current = current.next

            current.next = Node(data)

    def push(self, data):
        curr = Node(data)
        curr.next = self.head
        self.head = curr


    def insert_at(self, data, index):
        if index == 0:
            self.push(data)

        else:
            curr = self.head
            while index != 1:
                index -= 1
                curr = curr.next

            after = curr.next
            curr.next = Node(data)
            curr.next.next = after

    def insertEnd(self, data):
        curr = self.head
        while curr.next:
            curr = curr.next

        curr.next = Node(data)


    def traverse(self):
        current = self.head

        while current:
            print(current.data)
            current = current.next


    def deleteData(self, data):
        if self.head.data == data:
            self.head = self.head.next
            return

        else:
            prev = self.head
            curr = prev.next

            while curr:
                if curr.data == data:
                    prev.next = curr.next
                    del curr
                    return

                prev = curr
                curr = curr.next


    def deleteIndex(self, index):
        if index == 0:
            self.head = self.head.next
            return

        else:
            prev = self.head
            curr = prev.next

            while index != 1:
                prev = curr
                curr = curr.next
                index -= 1

            prev.next = curr.next
            del curr
            return

    def listlength(self):
        curr = self.head
        self.len = 0

        while curr:
            self.len += 1
            curr = curr.next

        return self.len


    def swapNode(self, x, y):
        if x == y:
            return


        prevy = None
        curry = None
        prevx = None
        currx = None

        prev = None
        curr = self.head
        flagx = True
        flagy = True

        while curr and (flagx or flagy):

            if curr.data == x:
                prevx = prev
                currx = curr
                flagx = False


            elif curr.data == y:
                prevy = prev
                curry = curr
                flagy = False

            prev = curr
            curr = curr.next


        if currx is None or curry is None:
            print("Not Found")
            return

        if prevx is None:
            self.head = curry

        else:
            prevx.next = curry

        if prevy is None:
            self.head = currx

        else:
            prevy.next = currx


        temp = currx.next
        currx.next = curry.next
        curry.next = temp

        return

    def revere(self):
        prev = None
        current = self.head

        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt

        self.head = prev

    def addNode(self, node: Node):
        if self.head is None:
            self.head = node
            return

        else:
            cur = self.head

            while cur.next:
                cur = cur.next

            cur.next = node
            return


def mergeTwolists(headone: Node, headtwo: Node):
    if headone is None or headtwo is None:
        return

    dumNode = Node(0)
    cur = dumNode

    while True:

        if headone is None:
            cur.next = headtwo
            break

        if headtwo is None:
            cur.next = headone
            break


        if headone.data<headtwo.data:
            cur.next = headone
            headone = headone.next


        else:
            cur.next = headtwo
            headtwo = headtwo.next

        cur = cur.next

    return dumNode.next





if __name__ == '__main__':
    ar = LinkedList()
    ar.insert(1)
    ar.insert(3)
    ar.insert(5)

    br = LinkedList()
    br.insert(2)
    br.insert(4)
    br.insert(6)


    mergeTwolists(ar.head, br.head)




