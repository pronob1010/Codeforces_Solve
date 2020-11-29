
#
# t= int(input())
# for i in range(t):
#     n, m, r, c = list(map(int, input().split()))
#
#     a1 = (n-r)+(m-c)
#     b2 = (abs(1-r)+abs(1-c))
#     b3 = (abs(n-r)+abs(1-c))
#     b4 = (abs(1-r)+abs(m-c))
#     b5= (abs(n-r)+abs(m-c))
#
#     r1 = max(a1,b2,b3,b4, b5)
#     print(r1)

t= int(input())
for i in range(t):
    n, k = list(map(int, input().split()))
    c = list(map(int, input().split()))

    day = 0
    f = {}
    for i in c:
        if i in f:
            f[i]+=1
        else:
            f[i]=1

    m = max(f, key=lambda x:f[x])

    r1 = len(c)- max(f.values())
    if r1%k ==0:
        day = r1//k
    else:
        day = (r1//k)+1
    print(day)