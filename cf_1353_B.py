t = int(input())
for j in range(t):
    n,k = list(map(int, input().split()))

    s = list(map(int, input().split()))
    s2 = list(map(int, input().split()))
    s.sort()
    s2.sort(reverse=True)

    for i in range(k):
        if s[i]<s2[i]:
            s[i]=s2[i]

    print(sum(s))


