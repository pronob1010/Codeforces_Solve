a, b = list(map(int,input().split()))
n = int(input())
for i in range(n):
    l_x = -101
    l_y = -101
    l_v = -101

    x,y,v = list(map(int,input().split()))

    if l_x>= x and l_y>=y and l_v<=v:
        l_x = x
        l_y = y
        l_v = v

print(l_x,l_y,l_v)