def longestIncreasingSubArray(arr):
    longest = 1
    length = 1

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            length += 1
        else:
            if longest < length:
                longest = length
            length = 1
    return longest


if __name__ == '__main__':
    arrNumber = [2, 3, 4, 5, 1, 9, 6]
    print(f"Value is longest increasing sub array is {longestIncreasingSubArray(arrNumber)}")
