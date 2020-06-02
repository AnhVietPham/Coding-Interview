def last_digit_of_large_fibonacci_number(n):
    a, b = 0, 1
    for _ in range(n - 1):
        c = a + b
        a, b = b, c
    return b % 10


if __name__ == '__main__':
    number = int(input().strip())
    print(last_digit_of_large_fibonacci_number(number))
