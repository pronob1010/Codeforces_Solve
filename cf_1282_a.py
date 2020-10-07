n = int(input())
res = 0
for z in range(n):
    a, b, c, r = list(map(int, input().split()))

    if (c >= a) and (c <= b):
        if a is b and b is c:
            print('0')
        else:
            res = ((max(a,b)-min(a,b))-r*2)
            print(res)

    else:
        if r > (c-max(a,b)):
            res = (max(a,b)-(r-(c-max(a,b))))-a
            print(res)
