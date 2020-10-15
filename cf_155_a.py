n = int(input())
s = list(map(int,input().split()))[:n]
l=[]
m = []
c = 0
l.append(s[0])
for i in range(1,n):
    l.append(s[i])
    if (min(l)== s[i] or max(l)==s[i]) and s[i] not in m:
        c+=1
        m.append(s[i])
print(m)
print(len(m))
