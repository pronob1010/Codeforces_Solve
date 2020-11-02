n,m = list(map(int, input().split()))
a = list(map(int, input().split()))[:m]
l1 = a.sort()
l2 = a

max = 0
j = 0

for i in range(1,n):
    if max(a)>i: