t = int(input())
for i in range(t):
    m1 = []
    m2=[]
    cou = 0
    r, c = list(map(int, input().split()))
    for j in range(r):
        cv = list(map(int, input().split()))[:c]
        for k in cv:
            m1.append(k)
    m1.sort()
    x = len(m1)//2
    print(m1[x])

    # m = max(m1)
    # for i in m1:
    #     if i<m or i>m:
    #         i = i+(m-i)
    #         cou += 1
    #     m2.append(i)
    #
    # print(cou*2)
    # print(m2)