# evaluate prefix expression
str = "10+3*5/(16-4)"


def prefixeval(arr: str):
    if arr is None:
        return

    arr = list(arr)

    stack = []
    operators = {"+", "-", "*", "/", "^"}

    while arr:
        op = arr.pop()

        if op.isdigit():
            stack.append(op)

        elif op in operators:
            op1 = int(stack.pop())
            op2 = int(stack.pop())

            if op == "+":
                stack.append(op1 + op2)

            elif op == "-":
                stack.append(op1 - op2)

            elif op == "*":
                stack.append(op1 * op2)

            elif op == "/":
                stack.append(op1 / op2)

            elif op == "^":
                stack.append(op1 ^ op2)

        if len(arr) == 0:
            return stack[0]


print(prefixeval(str))

# building a stack using Queue


class Stack:
    def __init__(self):
        self.q1 = []
        self.q2 = []

    def add(self, data):
        self.q2.append(data)

        while self.q1:
            self.q2.insert(0, self.q1.pop())

        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        return self.q1.pop()

