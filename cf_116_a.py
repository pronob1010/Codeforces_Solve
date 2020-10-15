t = int(input())
minc= 0
max = 0
for i in range(t):
    exit, enter = list(map(int,input().split()))
    minc += (enter - exit)
    if max<minc:
        max = minc
print(max)
