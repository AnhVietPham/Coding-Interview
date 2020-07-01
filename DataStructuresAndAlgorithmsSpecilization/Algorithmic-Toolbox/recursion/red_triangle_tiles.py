import sys

sys.setrecursionlimit(1500)


def red_triangle_tiles(n):
    if n == 1:
        return 12
    return 24 + (red_triangle_tiles(n - 1))


if __name__ == '__main__':
    layer = int(input())
    print(red_triangle_tiles(layer))
