t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))[:n]
    b = list(map(int, input().split()))[:n]
    c = list(map(int, input().split()))[:n]
    p = []
    f = 0
    f1 = 0
    f2 = 0

    p.append(a[0])
    for j in range(1,n):
        l = len(p)
        if f == 0 and a[j-1] != a[j]:
            p.append(a[j])

        if f == 0 and a[j - 1] == a[j]:
            p.append(b[j])
            f = 1

        if f == 1 and b[j-1] != b[j]:
            p.append(b[j])
            f = 1
        if f == 1 and b[j-1] == b[j]:
            p.append(c[j])
            f = 1
        if f == 1 and c[j-1] != c[j]:
            p.append(c[j])
            f = 0
        elif f == 2 and c[j-1] == c[j]:
            p.append(b[j])
            f = 1


    print("----")
    print(*p,sep=" ")


    # for j in range(0,n-1):
    #     l = len(p)
    #     if (a[j-1] != a[j]):
    #         if l <=n and p[l-1] != a[j-1]:
    #             f = 1
    #             p.append(a[j - 1])
    # if f == 0:
    #     p.append(a[0])
    #
    # for j in range(0, n - 1):
    #     l = len(p)
    #     if (b[j - 1] != b[j]):
    #         if l <= n and p[l - 1] != b[j - 1]:
    #             p.append(b[j - 1])
    #             f1 = 1
    # if f1 == 0:
    #     p.append(b[0])
    #
    # p.append(c[0])
    # for j in range(0, n - 1):
    #     l = len(p)
    #     if (c[j - 1] != c[j]):
    #         if l <= n and p[l - 1] != c[j - 1]:
    #             p.append(c[j - 1])
    #             f2 = 1
    # if f2 == 0:
    #     p.append(c[0])

    # print(p)

    # for j in range(1,n):
    #     if (f==0) and (a[j-1] == a[j]):
    #         f = 1
    #         l = len(p)
    #         if l>0 and p[l-1]!=a[j-1]:
    #             p.append(a[j - 1])
    #         else:
    #             p.append(a[j-1])
    #
    #     elif (a[j-1] != a[j]):
    #         l = len(p)
    #         if l > 0 and p[l - 1] != a[j - 1]:
    #             p.append(a[j - 1])
    #         else:
    #             p.append(a[j - 1])
    # print(p)
    #
    # for j in range(1,n):
    #     if (f1==0) and (b[j-1] == b[j]):
    #         f1 = 1
    #
    #         l = len(p)
    #         if l > 0 and p[l - 1] != b[j - 1]:
    #             p.append(b[j - 1])
    #         else:
    #             p.append(b[j - 1])
    #
    #     elif (b[j-1] != b[j]):
    #         l = len(p)
    #         if l > 0 and p[l - 1] != b[j - 1]:
    #             p.append(b[j - 1])
    #         else:
    #             p.append(b[j - 1])
    # print(p)
    #
    # for j in range(1,n):
    #     if (f2 == 0) and (c[j-1] == c[j]):
    #         f2 = 1
    #         l = len(p)
    #         if l > 0 and p[l - 1] != c[j - 1]:
    #             p.append(c[j - 1])
    #         else:
    #             p.append(c[j - 1])
    #     elif (c[j-1] != c[j]):
    #         l = len(p)
    #
    #         if l > 0 and p[l - 1] != c[j - 1]:
    #             p.append(c[j - 1])
    #         else:
    #             p.append(c[j - 1])
    # print(p)