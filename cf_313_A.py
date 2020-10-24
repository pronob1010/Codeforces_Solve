n = int(input())
if n>0:
    r = n
    print(r)
else:
    t1 = str(n)
    t2 = str(n)

    t1=int(t1[:-1])
    t2 = int(t2[:-2]+t2[-1])


    print(max(t1,t2))
    # print(t1)
    # print(t2)