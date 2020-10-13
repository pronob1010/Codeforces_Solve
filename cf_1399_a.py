for _ in range(int(input())):
    n = int(input())
    s = list(map(int,input().split()))[:n]
    c = 0
    if len(s)>1:
        for i in range(1,n):
            if abs(s[i-1]-s[i])<=1:
                c = 1
            else:
                c = 0
                break
    else:
        print("YES")
        break

    if c == 1:
        print("YES")
    else:
        print("NO")
