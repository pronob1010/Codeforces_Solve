n = int(input())
for i in range(n):
    a, b = list(map(int, input().split()))

    r = a

    if r%2==0:
        r+=2*(b)
    else:
        r+=r
        r += 2*(b-1)

    print(r)