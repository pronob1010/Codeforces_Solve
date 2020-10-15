t = int(input())
exit, enter = list(map(int,input().split()))
minc= (enter - exit)
max = minc
for i in range(t-1):
    exit, enter = list(map(int,input().split()))
    m = (minc-exit)+enter
    if max<m:
        max = m
print(max)

