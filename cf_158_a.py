a, b = list(map(int,input().split()))
r = list(map(int,input().split()))[:a]
c=0
che = r[b-1]
for i in range(len(r)):
    if 0<r[i] and r[i]>=che:
        c+=1

print(c)