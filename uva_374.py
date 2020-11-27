def bigmod(b, p, m):
    if p==0:
        return 1
    elif p == 1:
        return b%m
    else:
        x = bigmod(b,p//2,m)
        if p % 2==1:
            return (x*x*b)%m
        else:
            return (x * x) % m


while True:
    try:
        b = input()
        if b=="":
            b = int(input())
        else:
            b=int(b)

        p = int(input())
        m = int(input())


    except EOFError:
        break
    r = bigmod(b, p, m)
    print(r)