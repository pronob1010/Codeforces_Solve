lz = 0
lo = 0
rz = 0
ro = 0
for i in range(int(input())):
    l,r = list(map(int,input().split()))
    if l==0:
        lz+=1
    else:
        lo+=1
    if r==0:
        rz += 1
    else:
        ro += 1

print(min(lz,lo)+min(ro,rz))
