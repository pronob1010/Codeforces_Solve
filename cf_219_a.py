n = int(input())
s = input()
p = {}
for i in range(1,len(s)+1):
    if s[i-1] in p:
        p[s[i-1]]+=1
    else:
        p[s[i-1]] = 1
f=0
for i in p.values():
    if n==i:
        f=1
    else:
        f=0
        break

if f == 1:
    k = len(p.keys())
    klist = [str(i) for i in p.keys()]
    for i in range(len(s)//2):
        print(*klist, sep="",end="")

else:
    print("-1")