import math


def multiply(num1, num2):
    length_of_num1 = len(num1)
    length_of_num2 = len(num2)

    result = [0] * (length_of_num1 + length_of_num2)
    i_n1 = 0
    for i in range(length_of_num1 - 1, -1, -1):
        hold = 0
        i_n2 = 0
        digit_of_num1 = ord(num1[i]) - 48
        for j in range(length_of_num2 - 1, -1, -1):
            digit_of_num2 = ord(num2[j]) - 48
            sum_of_digit = digit_of_num1 * digit_of_num2 + result[i_n1 + i_n2] + hold
            hold = sum_of_digit // 10
            result[i_n1 + i_n2] = sum_of_digit % 10
            i_n2 += 1
        if hold > 0:
            result[i_n1 + i_n2] += hold
        i_n1 += 1
    length_of_result = len(result) - 1
    while length_of_result >= 0 and result[length_of_result] == 0:
        length_of_result -= 1

    if length_of_result == -1:
        return "0"

    result_of_multiplication = ""
    while length_of_result > 0:
        result_of_multiplication += chr(result[length_of_result] + 48)
        length_of_result -= 1
    return result_of_multiplication


if __name__ == '__main__':
    print(multiply('23958233', '5830'))
