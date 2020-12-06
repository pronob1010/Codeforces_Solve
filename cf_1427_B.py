t = int(input())
for i in range(t):
    n, k = list(map(int, input().split()))
    s = input()
    r = s.replace('L','W',k)
    print(s)
    print(r)

    f = 0
    ans = 0
    for i in range(len(r)):
        if r[i]=='W' and f==0:
            ans+=1
            f = 1
        elif r[i]=='W' and f == 1:
            ans+=2
            f = 1
        else:
            f = 0

    print(ans)