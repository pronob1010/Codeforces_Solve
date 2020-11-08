n = int(input())
a = list(map(int,input().split()))
m = 0
for i in a:
    c = 0
    for j in a:
        if j%i==0:
            c+=1
        if c>=m:
            m = c
            r = i
print(r)