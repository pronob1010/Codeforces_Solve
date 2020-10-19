k, n, w = list(map(int,input().split()))
r=0
for i in range(1,w+1):
    r+= k*i
if r<=n:
    print("0")
else:
    print(abs(r-n))
