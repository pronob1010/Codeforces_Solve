t = int(input())
for i in range(t):
    n = int(input())
    s = list(map(int, input().split()))[:n]
    rl=[]
    r = 0
    j = 1
    while(j<n+1):
        rl.append(-1*s[j])
        rl.append(s[j-1])
        # r += (s[j-1]*(-1*s[j]))
        # r += (s[j-1] * s[j])
        j+=2
    print(*rl, sep=" ")