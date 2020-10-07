n = int(input())
c=0
for i in range(n):
    a,b = list(map(int,input().split()))
    if (b-a)>=2:
        c+=1

print(c)