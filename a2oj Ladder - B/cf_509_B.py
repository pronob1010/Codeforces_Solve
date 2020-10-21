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

    for k in range(1,l+1):
        print(r)
        r = min(r,k+1-c1[k-1]+c2[k-1+1])
        r = min(r, c1[k-1] +(l-k-1-1)-c2[k-1 + 1])


    print(r)



