def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return int((a * b) / gcd(a, b))


if __name__ == '__main__':
    one, two = map(int, input().split(' '))
    print(lcm(one, two))
