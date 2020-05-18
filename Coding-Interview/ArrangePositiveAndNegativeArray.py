import random


def randomArr(length):
    randomList = []
    for i in range(0, length):
        randomList.append(random.randint(-5000, 5000))
    return randomList


if __name__ == '__main__':
    inputNumber = int(input().strip())
    arr = randomArr(inputNumber)
    print(arr)
    x = 0
    y = 0
    n = len(arr) - 1
    while x < n - y:
        if arr[x] < 0 and arr[n - y] >= 0:
            temp = arr[n - y]
            arr[n - y] = arr[x]
            arr[x] = temp
            x += 1
            y += 1
        elif arr[x] <= 0 and arr[n - y] <= 0:
            y += 1
        elif arr[x] >= 0 and arr[n - y] >= 0:
            x += 1
        elif arr[x] >= 0 and arr[n - y] <= 0:
            x += 1
            y += 1
    print(arr)