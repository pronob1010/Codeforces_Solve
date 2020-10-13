for j in range(int(input())):
    n = int(input())
    s = list(map(int,input().split()))[:n]
    s.sort()
    c = 0
    if n == 1:
        print("YES")

    else:
        for i in range(1,n):
            if abs(s[i]-s[i-1])<=1:
                c = 1
            else:
                c = 0
                break

        if c == 1:
            print("YES")
        else:
            print("NO")


