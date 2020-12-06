
t = int(input())
for i in range(t):
    n, k = list(map(int, input().split()))
    x = []
    y = []
    for j in range(n):
        p = list(map(int, input().split()))
        x.append(p[0])
        y.append(p[1])

    ll = len(x)
    c = 0
    f = 0
    for i in range(ll):
        c = 0
        for j in range(ll):
            if j == i:
                continue
            else:
                s = abs(x[i] - x[j]) + abs(y[i] - y[j])
                if s <= k:
                    c += 1
                else:
                    break

        if c==n-1 and f == 0:
            f = 1
            print(1)


    if f == 0:
        print(-1)

