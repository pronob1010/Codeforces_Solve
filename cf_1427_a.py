t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))[:n]
    b= []
    # i=2
    # while(i<=n):
    #     s = a[i-2] + a[i-1]
    #     if s!=0:
    #         b.append(a[i-2])
    #     else:
    #         a[i-1],a[i] = a[i],a[i-1]
    #     i += 1
    i = 2
    c = []
    b.append(a[0])
    while(i<=n):
        x = sum(b)
        ns = x + a[i-1]
        if x != 0 and ns != 0:
            b.append(a[i - 1])
        else:
            c.append(a[i-1])
        i += 1
    j = 1
    while (len(c)!=0 and sum(c)!= 0):
        fc = sum(b)
        if c[j-1]+fc != 0:
            b.append(c[j-1])
            c.remove(c[j-1])
        else:
            c.append(c[j-1])

    if sum(b) == 0:
        print("NO")
    else:
        print("YES")
        print(*b, sep=" ")



    # if sum(a)!=0:
    #     print(a)

    # c=0
    # for i in range(n):
    #     if a[i] == b[i]:
    #         c+=1
    #
    # if c == n:
    #     print("NO")
    # else:
    #     print("YES")
    #     print(*b,sep=" ")
