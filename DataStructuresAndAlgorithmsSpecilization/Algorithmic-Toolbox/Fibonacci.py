def fibonacci(number):
    if number <= 1:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)


if __name__ == '__main__':
    n = int(input().strip())
    f1 = 0
    f2 = 1
    a = 0
    arr_fibonacci = [1]
    for i in range(0, n):
        a = f1 + f2
        f1 = f2
        f2 = a
        arr_fibonacci.append(a)
    print(arr_fibonacci)
    print('\n')
    arr_fibonacci_recursion = []
    for i in range(1, n + 2):
        arr_fibonacci_recursion.append(fibonacci(i))
    print(arr_fibonacci_recursion)
