def design_string(msg, n):
    result_design_string = ''
    for _ in range(0, n):
        result_design_string += msg
    return result_design_string


if __name__ == '__main__':
    N, M = map(int, input().split(" "))
    center_col = M // 2
    center_row = N // 2
    result = ''
    count_pattern = 1
    temp = center_row
    # WELCOME
    print('Solution 1')
    for i in range(0, N):
        for j in range(0, M):
            if (center_col - (3 * i + 1) <= j <= center_col + (3 * i + 1) and i < center_row) or (
                    center_col - (3 * (temp - 1) + 1) <= j <= center_col + (
                    3 * (temp - 1) + 1) and i > center_row):
                if count_pattern == 1:
                    result += '.'
                    count_pattern += 1
                    continue
                if count_pattern == 2:
                    result += '|'
                    count_pattern += 1
                    continue
                if count_pattern == 3:
                    result += '.'
                    count_pattern = 1
                    continue
            elif center_row == i:
                if center_col - 3 <= j <= center_col + 3:
                    if count_pattern == 1:
                        result += "W"
                        count_pattern += 1
                        continue
                    if count_pattern == 2:
                        result += "E"
                        count_pattern += 1
                        continue
                    if count_pattern == 3:
                        result += 'L'
                        count_pattern += 1
                        continue
                    if count_pattern == 4:
                        result += 'C'
                        count_pattern += 1
                        continue
                    if count_pattern == 5:
                        result += 'O'
                        count_pattern += 1
                        continue
                    if count_pattern == 6:
                        result += 'M'
                        count_pattern += 1
                        continue
                    if count_pattern == 7:
                        result += 'E'
                        count_pattern = 1
                        continue
                else:
                    result += '-'
            else:
                result += '-'
        if i > center_row:
            temp -= 1
        result += '\n'
    print(result)

    print('Solution 2')
    for i in range(0, N):
        if i == center_row:
            msg_welcome = 'WELCOME'
            result_design_msg_welcome = design_string('-', center_col - len(msg_welcome) // 2) + msg_welcome + design_string('-', center_col - len(msg_welcome) // 2)
            print(result_design_msg_welcome)
        else:
            number_pattern = 2 * i + 1 if i < center_row else 2 * (N - i) - 1
            string_pattern = design_string('.|.', number_pattern)
            result_design_pattern = design_string('-',
                                                  center_col - len(
                                                      string_pattern) // 2) + string_pattern + design_string(
                '-', center_col - len(string_pattern) // 2)
            print(result_design_pattern)

    print('Solution 3')
    string1 = 'WELCOME'
    string2 = '.|.'
    list_string = [
        (string1.center(M, '-')) if i == center_row else (
                    string2 * (2 * i + 1 if i < center_row else 2 * (N - i) - 1)).center(M, '-')
        for i in range(0, N)]
    print(list_string)
    for i in list_string:
        print(i)
