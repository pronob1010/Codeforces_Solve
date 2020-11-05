for i in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))
    s2 = reversed(s)

    # l = len(s)
    # ns = []
    # ns2 = []
    # for l in range(1,l):
    #     s2[l-1],s2[l] = s2[l], s2[l-1]
    # print(s2)

    # for k in range(1,l):
    #     p = s[k-1]+s[k]
    #     ns.append(p)
    #
    # for k in range(1,l):
    #     p = s2[k-1]+s2[k]
    #     ns2.append(p)

    print(*s2)