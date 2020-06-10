if __name__ == '__main__':
    n, W = map(int, input().split())
    items = [tuple([int(v) for v in input().split()]) for _ in range(n)]
    items.sort(key=lambda x: x[0] / x[1], reverse=True)
    total_value = 0
    for v, w in items:
        if n == 1 and W >= w:
            print(v)
            quit()
        if W == 0:
            print(total_value)
            quit()
        min_weight = min(w, W)
        total_value += min_weight * v / w
        W -= min_weight
    print(total_value)
