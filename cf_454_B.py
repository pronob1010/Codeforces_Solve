n = int(input())
s = list(map(int, input().split()))[:n]

t = s
s0 = sorted(s)
c = 0
for i in range(n):
    if t[i-1]>t[i]:
        p = i
        c+=1
# print(c)
if t==s0:
    print(0)

else:
    if c>1:
        print(-1)
    else:
        print(n-p)