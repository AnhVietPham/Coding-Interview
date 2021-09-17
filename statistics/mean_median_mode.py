import numpy as np
from scipy import stats


def _mean(numbers):
    return sum(numbers) / len(numbers)


def _recursive_mean(numbers, s=0, i=0):
    if len(numbers) == i:
        return s / len(numbers)
    return _recursive_mean(numbers, s=s + numbers[i], i=i + 1)


def _recursive_mean_2(numbers, n):
    if n == 1:
        return numbers[0]
    return (_recursive_mean_2(numbers, n - 1) * (n - 1) + n) / n


def _median(numbers):
    arr_sort = np.sort(numbers)
    print(arr_sort)
    center = round(len(arr_sort) / 2)
    if len(arr_sort) % 2 == 0:
        median = (float(arr_sort[center - 1]) + float(arr_sort[center])) / 2.0
    else:
        median = arr_sort[center]
    return median


if __name__ == '__main__':
    size = int(input())
    arr = list(map(int, input().split()))
    print(f"Numpy: {np.mean(arr)}")
    print(f"Homemade mean: {_mean(arr)}")
    print(f"Homemade recursive mean: {_recursive_mean(arr)}")
    print(f"Homemade recursive mean2: {_recursive_mean_2(arr, len(arr))}")
    print(f"Numpy: {np.median(arr)}")
    print(f"Homemade median: {_median(arr)}")
    print(int(stats.mode(arr)[0]))
