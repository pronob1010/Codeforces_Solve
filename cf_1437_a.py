n = int(input())
for i in range(n):
    l,r = list(map(int, input().split()))
    r1 = (l+r)//2

    c1 = l % (r+1)

    c2 = (r+1)/2
    if c1>=c2:
        print("YES")
    else:
        print("NO")