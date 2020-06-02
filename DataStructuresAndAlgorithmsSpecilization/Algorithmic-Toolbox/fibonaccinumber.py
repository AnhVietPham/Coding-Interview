def fibonacci_number(number):
    a, b = 0, 1
    if number <= 0:
        quit()
    for _ in range(1, number):
        c = a + b
        a, b = b, c
    print(b)


if __name__ == '__main__':
    n = int(input().strip())
    fibonacci_number(n)
