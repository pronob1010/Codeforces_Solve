for i in range(int(input())):
    n = int(input())
    s = list(map(int,input().split()))[:n]

    for j in range(1,n):
        if s[j-1]!=s[j]:
            s[j-1]=sum(s[j-1],s[j])
            s[j] = sum(s[j - 1], s[j])

    print(s)