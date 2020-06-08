def last_digit_of_large_fibonacci_number(n):
    a, b = 0, 1
    for _ in range(n - 1):
        c = a + b
        a, b = b, c % 10
    return b


if __name__ == '__main__':
    number = int(input().strip())
    print(last_digit_of_large_fibonacci_number(number))
