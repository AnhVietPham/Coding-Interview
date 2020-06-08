def fibonacci(n, m):
    f0, f1 = 0, 1
    for _ in range(1, n):
        temp = f0
        f0, f1 = f1, f1 + temp
    return f1


if __name__ == '__main__':
    n, m = [int(i) for i in input().split()]
    print(fibonacci(n, m))
