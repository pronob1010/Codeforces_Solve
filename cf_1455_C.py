t = int(input())
for i in range(t):
    a, b = list(map(int, input().split()))
    if a<=1:
        a = 0
    else:
        a-=1
    print(a, b)
