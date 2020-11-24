t = int(input())
for i in range(t):
    n = int(input())
    r = []
    for i in range(1,n+1):
        r.append(i)
    # print(r)
    for i in range(1,n):
        r[i-1],r[i] = r[i],r[i-1]

    print(*r)