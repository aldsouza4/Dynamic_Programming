# class Solution:
#     def check(self, length, width, base_length, base_width):
#         if max(length, width) < max(base_length, base_width) \
#                 and min(length, width) < min(base_length, base_width):
#             return True
#         else:
#             return False
#
#     def maxHeight(self, height, width, length, n, base_length, base_width):
#         if n == 0:
#             return 0
#
#         op1 = op2 = op3 = -1
#
#         if self.check(height[n - 1], width[n - 1], base_length, base_width):
#             op1 = max(length[n - 1] + self.maxHeight(height, width, length, len(height), height[n - 1], width[n - 1]),
#                       self.maxHeight(height, width, length, n - 1, base_length, base_width))
#
#         if self.check(width[n - 1], length[n - 1], base_length, base_width):
#             op2 = max(height[n - 1] + self.maxHeight(height, width, length, len(height), width[n - 1], length[n - 1]),
#                       self.maxHeight(height, width, length, n - 1, base_length, base_width))
#
#         if self.check(length[n - 1], height[n - 1], base_length, base_width):
#             op3 = max(width[n - 1] + self.maxHeight(height, width, length, len(height), length[n - 1], height[n - 1]),
#                       self.maxHeight(height, width, length, n - 1, base_length, base_width))
#
#         return max([op1, op2, op3])


# x = Solution()
# n = 3
# height = [1, 4, 3]
# width = [2, 5, 4]
# length = [3, 6, 1]


# print(x.maxHeight(height, width, length, n, float('inf'), float('inf')))


def boxes(length: list, width: list, height: list):
    n = len(length)

    for i in range(n):
        length.append(height[i])
        width.append(width[i])
        height.append(length[i])

        length.append(length[i])
        width.append(height[i])
        height.append(width[i])

    return length, width, height


class Solution:
    def maxHeight(self, height, width, length, n):
        length, width, height = self.boxes(length, width, height)
        print(width)
        print(length)
        return self.maxheight(height, width, length, n, float('inf'), float('inf'))

    def boxes(self, length: list, width: list, height: list):
        n = len(length)

        for i in range(n):
            length.append(height[i])
            width.append(width[i])
            height.append(length[i])

            length.append(length[i])
            width.append(height[i])
            height.append(width[i])

        return length, width, height

    def check(self, length, width, base_length, base_width):
        if max(length, width) < max(base_length, base_width) \
                and min(length, width) < min(base_length, base_width):
            return True
        else:
            return False

    def maxheight(self, height, width, length, n, base_length, base_width):
        if n == 0:
            return 0

        if self.check(length[n - 1], width[n - 1], base_length, base_width):
            return max(height[n - 1] + self.maxheight(height, width, length, n, length[n - 1], width[n - 1]),
                       self.maxheight(height, width, length, n - 1, base_length, base_width), )
        else:
            return self.maxheight(height, width, length, n - 1, base_length, base_width)


x = Solution()
n = 2
height = [5, 3]
width = [2, 5]
length = [6, 3]

print(x.maxHeight(height, width, length, n))
