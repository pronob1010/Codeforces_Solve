t = int(input())
for i in range(t):
    n = int(input())
    aa = list(map(int, input().split()))
    c = 0
    for i in range(1, len(aa)):
        maxn = max(aa[i-1], aa[i])
        minn = min(aa[i-1], aa[i])

        while(maxn>minn*2):
            minn+=minn
            c += 1
    print(c)