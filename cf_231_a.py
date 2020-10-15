t = int(input())
s=0
for i in range(t):
    c = 0
    l = list(map(int, input().split()))

    for i in range(1,len(l)+1):
        if l[i-1]==1:
            c+=1
    if c>=2:
        s+=1

print(s)