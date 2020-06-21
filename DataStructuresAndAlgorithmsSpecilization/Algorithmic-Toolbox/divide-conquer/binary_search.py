def binary_search(array, value):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = int((left + right) // 2)
        if value == array[mid]:
            return mid
        else:
            if value < array[mid]:
                right = mid - 1
            else:
                left = mid + 1
    return -1


if __name__ == "__main__":
    arr = [int(i) for i in input().split()]
    x = int(input())
    print(binary_search(arr, x))
