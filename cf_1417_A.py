n = int(input())
for i in range(n):
    a,b = list(map(int,input().split()))
    a1 = list(map(int, input().split()))[:a]


    # s= 0
    # for j in a1:
    #     if j<a:
    #         s += j
    #
    # # print(s)
    #
    # if s<=b:
    #     print(s)
    #
    # s = 0


    s = 0
    l = 2
    le = len(a1)-1

    for k in range(le,0,-1):
        if l>0:
            s += a1[k]
            l -=1
        else:
            break

    print(s)

Failded