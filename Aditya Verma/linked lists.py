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

    def traverse(self, head):
        current = head

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
        """

        :param x:
        :param y:
        :return:No return, swaps the array in place itself
        """
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

    def getmiddle(self, head):
        """

        :param head:
        :return: returns the middle node
        """
        if head is None:
            return

        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def sortlists(self, a, b):
        if a is None:
            return b
        if b is None:
            return a

        result = None

        if a.data <= b.data:
            result = a
            result.next = self.sortlists(a.next, b)

        elif b.data <= a.data:
            result = b
            result.next = self.sortlists(a, b.next)

        return result

    def mergeSort(self, head):
        """

        :param head:
        :return: returns the head of the sorted list
        """
        if head is None or head.next is None:
            return head

        middle = self.getmiddle(head)
        middlenext = middle.next

        middle.next = None

        sorted_left = self.mergeSort(head)
        sorted_right = self.mergeSort(middlenext)

        res = self.sortlists(sorted_left, sorted_right)

        return res

    def reverseGroups(self, head, group):
        if head is None:
            return

        count = 0
        current = head
        prev = None
        nxt = None

        while current and count < group:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
            count += 1

        if nxt is not None:
            head.next = self.reverseGroups(nxt, group)

        return prev

    def detectloop(self):
        if self.head is None:
            return

        ptr1 = self.head
        ptr2 = self.head

        while ptr1 and ptr2 and ptr2.next:
            ptr1 = ptr1.next
            ptr2 = ptr2.next.next

            if ptr1 == ptr2:
                self.removeloop(ptr1)

                return True

        return False

    def removeloop(self, loopnode):
        if self.head is None:
            return

        pointerone = self.head

        while True:

            pointertwo = loopnode
            while pointertwo != pointerone and pointertwo.next != pointerone:
                pointertwo = pointertwo.next

            if pointertwo.next == pointerone:
                pointertwo.next = None
                return

            pointerone = pointerone.next

    def rotatelist(self, k):
        if self.head is None:
            return

        slowptr = self.head
        fastptr = self.head

        while k != 0 and fastptr:
            fastptr = fastptr.next
            k -= 1

        while fastptr.next:
            slowptr = slowptr.next
            fastptr = fastptr.next

        fastptr.next = self.head
        self.head = slowptr.next
        slowptr.next = None

    def addtwonums(self, head1, head2):
        if head1 is None:
            return head2
        if head2 is None:
            return head1

        prev = None
        temp = None
        carry = 0

        while head1 is not None or head2 is not None:
            f = 0 if head1 is None else head1.data
            s = 0 if head2 is None else head2.data

            sum = f + s + carry
            carry = 1 if sum > 10 else 0
            sum = sum if sum < 10 else sum % 10

            temp = Node(sum)

            if self.head is None:
                self.head = temp

            else:
                prev.next = temp

            prev = temp

            if head1 is not None:
                head1 = head1.next

            if head2 is not None:
                head2 = head2.next

        if carry > 0:
            temp.next = Node(carry)

        return self.head

    def isPalindrome(self, head):

        def makeduplicate(head):
            newl = LinkedList()

            while head:
                newl.insert(head.data)
                head = head.next

            return newl.head

        def revere(head):
            prev = None
            current = head

            while current:
                nxt = current.next
                current.next = prev
                prev = current
                current = nxt

            return prev

        dup = makeduplicate(head)
        revhead = revere(dup)

        while True:
            if head and revhead:
                if head.data != revhead.data:
                    return False

                head = head.next
                revhead = revhead.next

            if head is None and revhead is not None:
                return False

            if head is not None and revhead is None:
                return False

            if head is None and revhead is None:
                return True

    def joinLinkedlist(self, head):
        cur = self.head
        while cur.next:
            cur = cur.next

        cur.next = head
        return

    def findCommonNode(self, head):
        if self.head is None or head is None:
            return

        cur1 = self.head

        while cur1:

            cur2 = head

            while cur2:
                if cur1.data == cur2.data:
                    return cur1.data

                cur2 = cur2.next

            cur1 = cur1.next

        return False


class NodeSpecial:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.random = None


# Linked List class
class LinkedList_:

    # Function to initialize the Linked
    # List object
    def __init__(self):
        self.head = None

    def insert(self, data):
        if self.head is None:
            self.head = NodeSpecial(data)
            return

        else:
            current = self.head

            while current.next:
                current = current.next

            current.next = NodeSpecial(data)
            return

    def makeclone(self):
        if self.head is None:
            return

        curr = self.head

        while curr:
            nxt = curr.next
            temp = NodeSpecial(curr.data)
            curr.next = temp
            temp.next = nxt
            curr = nxt

        curr = self.head
        while curr is not None:
            if curr.random is not None:
                curr.next.random = curr.random.next
            curr = curr.next.next

        curr = self.head
        dum_root = curr.next

        while curr.next:
            temp = curr.next
            curr.next = curr.next.next
            curr = temp

        return dum_root

    def traverse(self, head):
        current = head

        while current:
            print(current.data)
            current = current.next


t = LinkedList_()
t.insert(1)
t.insert(2)
t.insert(3)
t.insert(4)
k = t.makeclone()
t.traverse(k)

if __name__ == '__main__':
    ar = LinkedList()
    ar.insert(1)
    ar.insert(2)
    ar.insert(3)
    ar.insert(4)
    ar.insert(5)
    ar.insert(6)
    ar.insert(7)
    ar.insert(8)


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

        if headone.data < headtwo.data:
            cur.next = headone
            headone = headone.next

        else:
            cur.next = headtwo
            headtwo = headtwo.next

        cur = cur.next

    return dumNode.next
