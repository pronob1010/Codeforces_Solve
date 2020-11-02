n = int(input())
for i in range(n):
    a, b = list(map(int, input().split()))

    r = a

    if r%2==0:
        r+=2*(b)
    else:
        for k in range(2, n+1):
            if r%k==0:
                r+=i
                break

        r += 2*(b-1)

    print(r)