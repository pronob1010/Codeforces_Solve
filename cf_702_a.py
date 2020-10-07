n  = int(input())
s = list(map(int, input().split()))[:n]
sb =0
c = []
for i in range(1,len(s)):
    if s[i-1]<s[i]:
        sb += 1
    else:
        c.append(sb)
        sb = 0
    c.append(sb)

if len(c)>0:
    print(max(c)+1)
else:
    print(sb+1)


