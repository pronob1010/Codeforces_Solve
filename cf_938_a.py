n = int(input())
s = list(input())
v = ['a','e','i','o','u','y']
ns =[]
ns.append(s[0])

for i in range(1,n):
    if not(s[i-1] in v and s[i] in v):
        ns.append(s[i])


print(*ns,sep="")


