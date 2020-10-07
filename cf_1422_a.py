t = int(input())
for i in range(t):
    a,b,c = list(map(int,input().split()))
    r = max(a,b,c)
    r2 = min(a,b,c)
    print(r+r2)