a,b=map(int,input().split())
l=[]
c=0
for i in range(a):
    l.append(int(input()))


s=set(l)
for i in s:
    if l.count(i)%2 != 0:
        c+=1
print(a-c//2)

