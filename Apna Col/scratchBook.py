class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.nextRight = None


def traverse(root: Node):
    if root is None:
        return

    traverse(root.left)
    print(root.data)
    traverse(root.right)


root = Node(4)
root.left = Node(2)
root.left.left = Node(1)
root.left.right = Node(3)
root.right = Node(6)
root.right.left = Node(5)
root.right.right = Node(7)

# root = Node(62)
# root.left = Node(16)
# root.right = Node(15)
# root.left.right = Node(8)
# root.left.right.right = Node(8)
# root.right.left = Node(4)
# root.right.right = Node(7)
# root.right.left.left = Node(4)

from collections import deque


class Solution:
    def helpaterp(self, hospital):
        self.hospital = hospital
        self.rows = len(hospital)
        self.cols = len(hospital[0])
        return self.spread_covid()

    def isvalid(self, i, j):
        return 0 <= i < self.rows and 0 <= j < self.cols

    def isdelim(self, temp):
        return temp[0] == -1 and temp[1] == -1

    def checkall(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.hospital[i][j] == 1:
                    return True
        return False

    def spread_covid(self):

        queue = deque()
        ans = -1

        for i in range(self.rows):
            for j in range(self.cols):
                if self.hospital[i][j] == 2:
                    queue.append([i, j])

        queue.append([-1, -1])

        while len(queue) != 0:
            if len(queue) == 1 and self.isdelim(queue[0]):
                break

            flag = False

            while not self.isdelim(queue[0]):
                temp = queue[0]

                if self.isvalid(temp[0] + 1, temp[1]) and self.hospital[temp[0] + 1][temp[1]] == 1:

                    if not flag:
                        ans, flag = ans + 1, True

                    self.hospital[temp[0] + 1][temp[1]] = 2
                    queue.append([temp[0] + 1, temp[1]])

                if self.isvalid(temp[0] - 1, temp[1]) and self.hospital[temp[0] - 1][temp[1]] == 1:

                    if not flag:
                        ans, flag = ans + 1, True

                    self.hospital[temp[0] - 1][temp[1]] = 2
                    queue.append([temp[0] - 1, temp[1]])

                if self.isvalid(temp[0], temp[1] + 1) and self.hospital[temp[0]][temp[1] + 1] == 1:

                    if not flag:
                        ans, flag = ans + 1, True

                    self.hospital[temp[0]][temp[1] + 1] = 2
                    queue.append([temp[0], temp[1] + 1])

                if self.isvalid(temp[0], temp[1] - 1) and self.hospital[temp[0]][temp[1] - 1] == 1:

                    if not flag:
                        ans, flag = ans + 1, True

                    self.hospital[temp[0]][temp[1] - 1] = 2
                    queue.append([temp[0], temp[1] - 1])

                queue.popleft()

            queue.popleft()
            queue.append([-1, -1])

        if self.checkall():
            return -1

        return ans + 1
