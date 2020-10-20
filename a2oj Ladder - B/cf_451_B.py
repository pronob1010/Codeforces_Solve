n = int(input())
s = list(map(int,input().split()))
nl=[]
c=0
t =sorted(s)
for i in range(1,len(s)+1):
    if s[i-1]!= t[i-1]:
        c+=1
        nl.append(t[i-1])
if c==len(s) or c==0:
    print("no")
else:
    print("yes")
    print(*nl,sep=" ")

