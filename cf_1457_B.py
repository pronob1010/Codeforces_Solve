
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




    # x = 0
    # for i in c:
    #     if i is not m:
    #         # print(i)
    #         if x<=k:
    #             x += 1
    #         else:
    #             x-=k
    #             if x % k:
    #                 day += 1
    #             x = 0
    #     else:
    #         print(x, day)
    #         if x>0:
    #             day+=1
    #         x = 0
    # print(day)
