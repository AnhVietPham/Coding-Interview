if __name__ == '__main__':
    n, W = map(int, input().split())
    items = [tuple([int(v) for v in input().split()]) for _ in range(n)]
    print(items)
    items.sort(key=lambda x: x[0] / x[1], reverse=True)
    print(items)
    total_value = 0
    for v, w in items:
        if W == 0:
            print(total_value)
            quit()
        min_weight = min(w, W)
        total_value += min_weight * v / w
        W -= min_weight
