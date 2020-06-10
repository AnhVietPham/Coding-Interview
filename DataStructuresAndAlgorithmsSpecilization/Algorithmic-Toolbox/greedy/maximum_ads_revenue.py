if __name__ == '__main__':
    n = int(input())
    a = [int(i) for i in input().split()][:n]
    b = [int(i) for i in input().split()][:n]
    a.sort(reverse=True)
    b.sort(reverse=True)
    total_value = sum([a[i] * b[i] for i in range(n)])
    # for i in range(n):
    #     total_value += a[i] * b[i]
    print(total_value)

