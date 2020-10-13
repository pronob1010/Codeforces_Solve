for _ in range(int(input())):
    n  = int(input())
    s = list(map(int, input().split()))[:n]

    c = 0
    ns = []
    for i in range(2,n-1):
        if s[i-1]<s[i]>s[i+1]:
            c = 0
            print("YES")
            print(s[i-1],s[i],s[i+1])
            break
        else:
            c = 1
    if c == 1:
        print("NO")
    print()
