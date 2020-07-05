import sys

sys.setrecursionlimit(1500)


def ackermann_function(x, y):
    if x == 0:
        return y + 1
    if y == 0:
        return ackermann_function(x - 1, 1)
    return ackermann_function(x - 1, ackermann_function(x, y - 1))


if __name__ == '__main__':
    m, n = map(int, input().split())
    print(ackermann_function(m, n))
