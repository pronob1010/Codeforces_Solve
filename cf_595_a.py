n,m = list(map(int,input().split()))
c =0
for i in range(n):
    s = list(map(int,input().split()))[:2*m]
    for j in range(1,2*m,2):
        if s[j-1] == 1 or s[j] == 1:
            c+=1


print(c)