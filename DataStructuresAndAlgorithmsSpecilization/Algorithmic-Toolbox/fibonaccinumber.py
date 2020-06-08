def fibonacci_number(number):
    a, b = 0, 1
    if number <= 0:
        print(0)
        quit()
    for _ in range(1, number):
        c = a + b
        a, b = b, c
    print(b)
    print(b % 5)


if __name__ == '__main__':
    n = int(input().strip())
    fibonacci_number(n)
