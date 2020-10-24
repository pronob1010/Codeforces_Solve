n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

c = 0
l = []
f = {}
for i in range(1,n+1):
    for j in range(1,m+1):
        if b[j-1]>1<a[i-1] and b[j-1]%a[i-1]==0:
            p = b[j-1]//a[i-1]
            if p>0:
                l.append(p)
                
m = max(l)
for i in a:
    if i*m in b:
        c+=1
print(c)