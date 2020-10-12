for _ in range(int(input())):
    n, m , k = list(map(int,input().split()))
    e = n//k
    p = 0
    if e>m:
        p = m
    else:
        p = m - e

    print(p)