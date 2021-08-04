class Solution:
    def helpaterp(self, hospital):
        self.hospital = hospital
        self.rows = len(hospital)
        self.cols = len(hospital[0])

    def checkall(self, hospital):
        for i in range(len(hospital)):
            for j in range(len(hospital[0])):
                if hospital[i][j] == 1:
                    return True

        return False

    def isvalid(self, i, j):
        return 0 <= i < self.rows and 0 <= j < self.cols

    def isdelim(self, item):
        return item[0] == -1 and item[1] == -1

    def counttime(self, hospital):
        ans = 0
        queue = []

        for i in range(len(hospital)):
            for j in range(len(hospital[0])):
                if int(hospital[i][j]) == 1:
                    queue.append([i, j])

        queue.append([-1, -1])

        while queue:
            if len(queue) == 1 and self.isdelim(queue[0]):
                break

            flag = False

            while not self.isdelim(queue[0]):

                temp = queue.pop(0)

                if self.isvalid(temp[0]+1, temp[1]) and hospital[temp[0]+1][temp[1]] == 1:
                    if flag is False:
                        ans, flag = ans+1, True

                    hospital[temp[0]+1][temp[1]] = 2
                    queue.append([temp[0]])

