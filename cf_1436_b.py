for i in range(int(input())):
    n = int(input())

    p= []
    t = n-1
    for j in range(n):
        m = [0 for i in range(n)]

        for k in range(n):
            if t==k or k==t-1:
                m[t]=1
                m[t-1]=1
        t -= 1
        p.append(m)

    # p = []
    # t = n - 1

    # for j in range(n):
    #     m = []
    #     for k in range(n):
    #         if j==k or k==t:
    #             m.append(1)
    #         else:
    #             m.append(0)
    #     t -= 1
    #     p.append(m)

    for l in p:
        print(*l, sep=" ")
