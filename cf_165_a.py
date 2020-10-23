c = 0
for i in range(int(input())):
    a,b = map(int, input().split())
    if (a!=0 and b!=0) or (a==0 and b==0):
        x =abs(a-b)
        if x==1 or x ==0:
            c+=1

print(c)