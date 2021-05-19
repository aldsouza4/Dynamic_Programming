# Given the total number of persons n and a number k which indicates that k-1 persons are
# skipped and kth person is killed in circle. The task is to choose the place in the initial circle
# so that you are the last one remaining and so survive.'


def josephus(n, k):
    people = [i for i in range(1, n+1)]


    def kill_persons(people: list, k, start=0):
        if len(people) == 1:
            return people[0]

        kill = (start + k - 1) % len(people)
        people.pop(kill)
        return kill_persons(people, k, kill+1)


    return kill_persons(people, k-1)


print(josephus(40, 7))



