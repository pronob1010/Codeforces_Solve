for i in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))
    # fir = s[0]
    m = max(s)
    f = 0
    r = 0
    x = 0
    if s[0]==m and  s[1]<m:
        print(1)
    elif (s[len(s)-1]==m and s[len(s)-2]!=m):
        print(len(s))
    else:
        for j in range(1,len(s)-1):
            if s[j]==m and (s[j-1]!=m or s[j+1]!=m):
                print(j+1)
                break
        else:
            print(-1)


