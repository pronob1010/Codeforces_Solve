k, n, w = list(map(int,input().split()))
r=0
for i in range(1,w+1):
    r+= k*i

print(abs(r-n))
