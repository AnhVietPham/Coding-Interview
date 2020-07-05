def fibonacci(number):
    if number <= 1:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)


def fibonacci1(number1):
    fib_history = {1: 1, 0: 1}
    var = fib_history[0]
    print(fib_history)
    print(var)


if __name__ == '__main__':
    fibonacci1(1)
    # n = int(input().strip())
    # f1 = 0
    # f2 = 1
    # total = 0
    # arr_fibonacci = [1]
    # for i in range(0, n):
    #     total = f1 + f2
    #     f1 = f2
    #     f2 = total
    #     arr_fibonacci.append(total)
    # print(arr_fibonacci)
    # print('\n')
    # arr_fibonacci_recursion = []
    # for i in range(1, n + 2):
    #     arr_fibonacci_recursion.append(fibonacci(i))
    # print(arr_fibonacci_recursion)
