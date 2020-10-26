n = int(input())
for i in range(n):
    x = int(input())
    s = list(map(int,input().split()))[:x]
    s.sort()
    a =[]
    b =[]
    j =2
    #print(s)
    while(j<len(s)+1):
        if s[j-2]==s[j-1]:
            a.append(s[j-2])
            b.append(s[j-1])
            j +=2
        else:
            a.append(s[j-2])
            j+=1
    a.append(s[len(s)-1])

    mexA = 0
    mexB = 0

    # print(a)
    # print(b)

    if len(a) > 0:
        # print(max(a)+1)
        for k in range(max(a)+2):
            if k not in a:
                # print(k)
                mexA = k
                break
    if len(b)>0:
        for k in range(max(b)+2):
            if k not in b:
                mexB = k
                break

    # print(mexA, mexB)
    print(mexA+mexB)
