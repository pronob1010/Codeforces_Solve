k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())

r = 0

for j in range(1,d+1):
    if j%l==0 or j%m==0 or j%n==0 or j%k==0:
        r+=1
print(r)
