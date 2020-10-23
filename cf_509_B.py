for i in range(int(input())):
    n = input()
    l = len(n)
    c1 = []
    c2 = []
    o1=0
    o2 =0

    for j in range(1,l+1):
        if n[j-1]=='1':
            o1+=1
            c1.append(o1)
            c2.append(o2)
        else:
            o2+=1
            c2.append(o2)
            c1.append(o1)
    r =0
    # print(c1)
    # print(c2)
    li=[]
    o11=0
    o20=0
    for k in range(l):
        if n[k]=='1':
            o11+=1
        else:
            o20+=1

        # print(o20+o1-o11, o11+o2-o20)
        li.append(min(o20+o1-o11, o11+o2-o20))
    print(min(li))



