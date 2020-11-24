t = int(input())
for l in range(t):
    x, y = list(map(int, input().split()))

    mm = []
    f = 0
    g = 0
    for i in range(x):
        s = input()
        ms = []
        c = 0
        for j in range(len(s)):
            if s[j]=='*':
                c+=1
        mm.append(c)
    r = 0
    mm.sort()
    # print(mm)
    for i in range(len(mm)-1):
        if mm[i]==0:
            r+=1
        elif mm[i]>1 and mm[i]<y:
            r+=0

    r+=(y-mm[len(mm)-1])
    print(r)

    #     if c>=1 and c<y:
    #         f +=1
    #     elif c == y:
    #         g +=1
    # print(f,g)



