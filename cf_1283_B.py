t = int(input())
for _ in range(t):
    a,b = list(map(int, input().split()))

    rem = a//b
    rem2 = b* rem
    rem3 = a - rem2
    d = b//2

    if (rem3>= d):
        ans = rem2+d
    else:
        ans = rem2 + rem3

    print(int(ans))
