n, m = list(map(int, input().split()))
if m>n:
    print(-1)
else:
    r = (n//2)+(n%2)

    while r % m != 0:
        r+=1
    print(r)