for _ in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))[:n]
    for i in range(n):
        if i%2==0:
            if s[i]<0:
                s[i]*=-1
        else:
            if s[i]>0:
                s[i]*=-1
    print(*s,sep=" ")

    # nL = []
    # for i in range(1,len(s)):
    #     p = []
    #     p.append(s[i-2])
    #     p.append(s[i])
    #     nL.append(p)
    #
    # nllen = len(nL)
    # s = 0
    # ls = 0
    # for i in range(nllen//2):
    #     s+=sum(nL[i])
    #
    # if s>0:
    #     for i in range((nllen//2)+1,nllen):
    #         ls+=sub(nL[i])
    #
    #
    # print(nL)
    # print(nllen[i][0])
    # print(s,ls)
