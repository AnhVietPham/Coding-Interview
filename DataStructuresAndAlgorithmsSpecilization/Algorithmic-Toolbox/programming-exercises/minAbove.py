import sys

MAX = sys.maxsize


def minAboveSolution(arr, k):
    minAbove = 0
    minDistance = MAX
    for i in range(0, len(arr)):
        if 0 < arr[i] - arr[k] < minDistance:
            minDistance = arr[i] - arr[k]
            minAbove = arr[i]
    return minAbove


def minAboveSolution2(arr, k):
    minAbove = MAX
    for i in range(0, len(arr)):
        if arr[i] > arr[k]:
            minAbove = arr[i] if minAbove > arr[i] else minAbove
    return minAbove


if __name__ == '__main__':
    arrNumber = [5, 3, 6, 4, 8, 11, 0]
    print(minAboveSolution(arrNumber, 6))
    print(minAboveSolution2(arrNumber, 6))
