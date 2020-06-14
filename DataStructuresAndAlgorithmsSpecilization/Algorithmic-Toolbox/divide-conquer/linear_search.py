def linear_search(array, value, length):
    array.append(value)
    i = 0
    while array[i] != value:
        i += 1
    if i == length:
        print("Value does not have in array!")
    else:
        print("Value {} has in array at position {}".format(value, i))


if __name__ == '__main__':
    n = int(input())
    arr = [int(i) for i in input().split()][:n]
    x = int(input())
    linear_search(arr, x, n)
