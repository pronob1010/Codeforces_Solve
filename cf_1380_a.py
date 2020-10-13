for _ in range(int(input())):
    n  = int(input())
    s = list(map(int, input().split()))[:n]
    for i in range(1,n-1):
        if s[i-1]<s[i] and s[i]>s[i+1]:
            print("YES")
            print(i,i+1,i+2)
            break
    else:
        print("NO")

