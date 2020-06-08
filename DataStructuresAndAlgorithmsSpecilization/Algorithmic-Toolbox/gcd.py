def normalGCD(a1, b1):
    greatest = 0
    largest = b1 if a1 >= b1 else a1
    for i in range(1, largest + 1):
        if a1 % i == 0 and b1 % i == 0:
            greatest = i
    return greatest


def euclidGCD(a1, b1):
    numberOne = a1
    numberTwo = b1
    while numberOne != numberTwo:
        if numberOne > numberTwo:
            numberOne = numberOne - numberTwo
        else:
            numberTwo = numberTwo - numberOne
    return numberTwo


def euclidGCD2(a1, b1):
    while b1 != 0:
        temp = a1 % b1
        a1 = b1
        b1 = temp
    return a1


def euclidRecursionGCD(a1, b1):
    if b1 == 0:
        return a1
    return euclidRecursionGCD(b1, a1 % b1)


if __name__ == '__main__':
    a, b = map(int, input().split(' '))
    if a > b:
        print(euclidGCD2(a, b))
    else:
        print(euclidGCD2(b, a))
