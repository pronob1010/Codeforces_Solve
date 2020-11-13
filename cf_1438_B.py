t = int(input())
for i in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    s = []
    for i in p:
        s.append(2**i)
    s.sort()
    # print(s[0:len(s)])
    r = sum(s[0:len(s)-1])
    if r == s[len(s)-1]:
        print("YES")
    else:
        print("NO")