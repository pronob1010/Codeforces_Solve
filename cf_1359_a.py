for _ in range(int(input())):
    n, m , k = list(map(int,input().split()))
    e = n//k
    p = 0
    if e>=m:
        p = m
    else:
        m-= e
        if m>1:
            p = e-(m-1)
        else:
            p = e - (m)
    print(p)