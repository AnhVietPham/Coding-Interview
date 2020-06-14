import string


def solution1(n):
    alphabet = string.ascii_lowercase
    col = 4 * n - 3
    row = n * 2 - 1
    center_col = col // 2
    center_row = row // 2
    print(alphabet)
    for i in range(0, row):
        s = ''
        for j in range(0, col):
            if i < center_row:
                if center_col - (2 * i) <= j <= center_col + (2 * i):
                    if j == center_col:
                        s += alphabet[n - 1 - i]
                    elif j < center_col:
                        if j % 2 == 0:
                            s += alphabet[int(n - 1 - i + (n - 1 - j / 2))]
                        else:
                            s += '-'
                    else:
                        if j % 2 == 0:
                            s += alphabet[int(n - 1 - i + (n - 1 - (col - 1 - j) / 2))]
                        else:
                            s += '-'
                else:
                    s += '-'
            elif i == center_row:
                if j == center_col:
                    s += alphabet[n - 1 - i]
                elif j < center_col:
                    if j % 2 == 0:
                        s += alphabet[int(n - 1 - i + (n - 1 - j / 2))]
                    else:
                        s += '-'
                else:
                    if j % 2 == 0:
                        s += alphabet[int(n - 1 - i + (n - 1 - (col - 1 - j) / 2))]
                    else:
                        s += '-'
            else:
                if center_col - (2 * (row - 1 - i)) <= j <= center_col + (2 * (row - 1 - i)):
                    if j == center_col:
                        s += alphabet[n - 1 - (row - 1 - i)]
                    elif j < center_col:
                        if j % 2 == 0:
                            s += alphabet[int(n - 1 - (row - 1 - i) + (n - 1 - j / 2))]
                        else:
                            s += '-'
                    else:
                        if j % 2 == 0:
                            s += alphabet[int(n - 1 - (row - 1 - i) + (n - 1 - (col - 1 - j) / 2))]
                        else:
                            s += '-'
                else:
                    s += '-'
        print(s)


def solution2(n):
    alphabet = string.ascii_lowercase
    col = 4 * n - 3
    row = n * 2 - 1
    center_col = col // 2
    center_row = row // 2
    print(alphabet)
    for i in range(0, row):
        result = ''
        for j in range(0, col):
            if i <= center_row:
                if (center_col - (2 * i) <= j <= center_col + (2 * i)) and (j % 2 == 0):
                    result += alphabet[
                        center_col - int(j / 2) - i if j <= center_col else center_col - int((col - 1 - j) / 2) - i]
                else:
                    result += '-'
            else:
                if (center_col - (2 * (row - 1 - i)) <= j <= center_col + (2 * (row - 1 - i))) and (j % 2 == 0):
                    result += alphabet[
                        center_col - int(j / 2) - (row - 1 - i) if j <= center_col else center_col - int(
                            (col - 1 - j) / 2) - (row - 1 - i)]
                else:
                    result += '-'
        print(result)


def solution3(n):
    if n < 1 or n > 21:
        print("Too limited")
        quit()
    alphabet = string.ascii_lowercase
    col = 4 * n - 3
    row = 2 * n - 1
    for i in range(0, row):
        designAlphabet = ''
        begin = n - i - 1 if i < row / 2 else i - n + 1
        for j in range(begin, n):
            character = alphabet[j]
            designAlphabet = designAlphabet + character if designAlphabet == '' \
                else character + '-' + designAlphabet + '-' + character
        pattern = '-' * (int((col - len(designAlphabet)) / 2))
        print(pattern + designAlphabet + pattern)


def pythonSolution(n):
    alphabet = string.ascii_lowercase
    col = 4 * n - 3
    result = []
    for i in range(n):
        txt = '-'.join(alphabet[i:n])
        result.append((txt[::-1] + txt[1:]).center(col, '-'))
    print('\n'.join(result[::-1] + result[1:]))


if __name__ == '__main__':
    size = int(input())
    print("Solution 1")
    solution1(size)
    print("Solution 2")
    solution2(size)
    print("Python Solution")
    pythonSolution(size)
    print("Solution 3")
    solution3(size)
