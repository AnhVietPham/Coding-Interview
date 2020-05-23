import random


def randomArr(n):
    arr = []
    for _ in range(0, n):
        arr.append(random.randint(-5000, 5000))
    return arr


if __name__ == '__main__':
    input_n = int(input().strip())
    int_arr_number = randomArr(input_n)
    length = len(int_arr_number)

    print('Solution 1 Nested loop O(n^2): ')
    number_one = int_arr_number[0]
    number_two = int_arr_number[1]
    max_pair_wise = 0
    for i in range(1, len(int_arr_number)):
        for j in range(i + 1, len(int_arr_number)):
            if int_arr_number[i] * int_arr_number[j] > number_one * number_two:
                number_one = int_arr_number[j]
                number_two = int_arr_number[i]

    print(number_one)
    print(number_two)
    print(number_one * number_two)

    print('Solution 2 O(n): ')
    print(':(( This solution just solves case that array has  a second largest element to left of first largest '
          'element in array. Failed!')
    first_positive_number = 0
    second_positive_number = 0
    first_negative_number = 0
    second_negative_number = 0

    for i in range(0, len(int_arr_number)):
        if int_arr_number[i] >= 0 and first_positive_number <= int_arr_number[i]:
            second_positive_number = first_positive_number
            first_positive_number = int_arr_number[i]

        if int_arr_number[i] <= 0 and first_negative_number >= int_arr_number[i]:
            second_negative_number = first_negative_number
            first_negative_number = int_arr_number[i]

    if first_positive_number * second_positive_number >= first_negative_number * second_negative_number:
        print(first_positive_number)
        print(second_positive_number)
        print(first_positive_number * second_positive_number)
    else:
        print(first_negative_number)
        print(second_negative_number)
        print(first_negative_number * second_negative_number)

    print('Solution 3: Using sorted in python:')
    sorted_arr_number = sorted(int_arr_number)
    len_arr = len(sorted_arr_number) - 1
    print(sorted_arr_number)
    if sorted_arr_number[0] * sorted_arr_number[1] > sorted_arr_number[len_arr] * sorted_arr_number[len_arr - 1]:
        print(sorted_arr_number[0])
        print(sorted_arr_number[1])
        print(sorted_arr_number[0] * sorted_arr_number[1])
    else:
        print(sorted_arr_number[len_arr])
        print(sorted_arr_number[len_arr - 1])
        print(sorted_arr_number[len_arr] * sorted_arr_number[len_arr - 1])

    print('Solution 4: Just positive number. ')
    max_index1 = -1
    for i in range(0, length):
        if max_index1 == -1 or int_arr_number[i] > int_arr_number[max_index1]:
            max_index1 = i

    max_index2 = -1
    for i in range(0, length):
        if (i != max_index1) and (max_index2 == -1 or int_arr_number[i] > int_arr_number[max_index2]):
            max_index2 = i

    print(int_arr_number[max_index1])
    print(int_arr_number[max_index2])
    print(int_arr_number[max_index1] * int_arr_number[max_index2])
