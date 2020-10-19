for _ in range(int(input())):
    n = int(input())
    s= list(map(int,input().split()))
    s.sort()
    print(s)
    i=1
    j=1
    c=0
    forcheck=[]
    t = s[i - 1] + s[len(s) - j]
    while(i-1<len(s)-j):
        if t<=2*n and t == s[i-1]+s[len(s)-j]:
            if s[len(s)-j] not in forcheck:
                forcheck.append(s[len(s)-j])
                t = s[i - 1] + s[len(s) - j]
                print(s[i - 1],i-1, s[len(s) - j],len(s)-j)
                c+=1
                i+=1
                j+=1
        else:
            j+=1

    print(c)