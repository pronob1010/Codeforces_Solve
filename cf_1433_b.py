for i in range(int(input())):
    n = int(input())
    s = list(map(int,input().split()))
    z=[]
    f = 0
    for i in range(1,len(s)+1):
        if s[i-1]==1:
            z.append(i-1)

    # print(z)
    for j in range(2,len(z)+1):
        f +=(z[j-1]-z[j-2]-1)
    print(f)

