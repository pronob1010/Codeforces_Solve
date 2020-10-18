al=[]
bl=[]

for i in range(int(input())):
    a,b = list(map(int, input().split()))
    al.append(a)
    bl.append(b)

c = 0

for i in range(len(al)):
    for j in range(len(bl)):
        if al[i]==bl[j]:
            c+=1

print(c)

