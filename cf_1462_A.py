
p = int(input())
for l in range(p):
    n = int(input())
    s = list(map(int, input().split()))
    s2 = []
    j = 0
    for i in range(len(s)):
        p = s[i]
        q = s[len(s)-1-i]
        s2.append(p)
        s2.append(q)

    for i in range(len(s2)//2):
        print(s2[i],end=" ")
    print()
