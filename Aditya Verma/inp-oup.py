def all_substring(inp, oup=""):
    if inp == "":
        print(oup)
        return

    op1 = oup
    op2 = oup + inp[0]

    inp = inp[1:]

    all_substring(inp, op1)
    all_substring(inp, op2)


# all_substring("abc")

def unique_subsets(inp):
    map = []

    def uniq_subs(inp, oup=""):
        if inp == "":
            map.append(oup)
            return

        op1 = oup
        op2 = oup + inp[0]

        inp = inp[1:]

        uniq_subs(inp, op1)
        uniq_subs(inp, op2)

    uniq_subs(inp)
    memo = {}
    for i in map:
        if i not in memo:
            memo[i] = i

    return list(memo.keys())


# print(unique_subsets("abc"))


# Permutations with spaces

def spacePermut(inp, oup=""):
    if inp == "":
        print(oup)
        return

    op1 = oup + " " + inp[0]
    op2 = oup + inp[0]

    inp = inp[1:]

    spacePermut(inp, op1)
    spacePermut(inp, op2)


# for "ABCDEFG"
# spacePermut("BCDEFG", "A")


# Print all permutations of a string keeping the sequence but changing cases.

def casePermut(inp: str, oup=""):
    if inp == "":
        print(oup)
        return

    op1 = oup + inp[0].upper()
    op2 = oup + inp[0]

    inp = inp[1:]

    casePermut(inp, op1)
    casePermut(inp, op2)


# print(casePermut("ab"))

# Given a string S, we can transform every letter individually to be lowercase or
# uppercase to create another string.  Return a list of all possible strings we could create.

def lettrCase(inp: str, oup=""):
    if inp == "":
        print(oup)
        return

    if inp[0].isnumeric():
        op = oup + inp[0]
        inp = inp[1:]
        lettrCase(inp, op)

    elif inp[0].isalpha():
        op1 = oup + inp[0].upper()
        op2 = oup + inp[0].lower()

        inp = inp[1:]

        lettrCase(inp, op1)
        lettrCase(inp, op2)


# print(lettrCase("a1b"))

# Given n pairs of parentheses, write a function to generate all combinations of
# well-formed parentheses of length 2*n.


def balanceBracket(open, close, oup):
    if open == 0 and close == 0:
        print(oup)
        return

    if open != 0:
        op1 = oup
        op1 += "("
        balanceBracket(open - 1, close, op1)

    if close > open:
        op2 = oup
        op2 += ")"
        balanceBracket(open, close - 1, op2)


# for n = 3
# balanceBracket(2, 3, "(")

# Given a positive integer N, print all N bit binary numbers
# having more 1’s than 0’s for any prefix of the number.

def nbinary(n):
    op = "1"

    def prefixOne(oup, ones, zeroes, n):
        if n == 0:
            print(oup)
            return

        if ones == zeroes:
            op1 = oup + "1"
            prefixOne(op1, ones + 1, zeroes, n - 1)

        elif ones > zeroes:

            op2 = oup + "0"
            op3 = oup + "1"

            prefixOne(op2, ones, zeroes + 1, n - 1)
            prefixOne(op3, ones + 1, zeroes, n - 1)

    prefixOne(op, 1, 0, n - 1)


# nbinary(4)
