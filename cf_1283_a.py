t = int(input())
for _ in range(t):
    h,m = list(map(int,input().split()))
    r = 0


    if h is 0:
        h = 23
        m = 60 - m
        r = (h * 60) + m
        print(r)

    elif h is 23:
        m = 60 - m
        r = m
        print(r)

    elif h>0 and h<23:
        h = 24 - h-1
        m = 60 - m
        r = (h * 60) + m
        print(r)
