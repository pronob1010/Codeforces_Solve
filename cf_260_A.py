a,b,n = list(map(int, input().split()))
r = ''
r+=str(a)
for i in range(n):
    j=1
    while True:
        p = r+str(j)
        if int(p)%b==0:
            r = r+str(j)
            break
        else:
            j += 1
    # print(r)

print(r)
