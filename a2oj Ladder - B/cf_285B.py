n ,s , t= list(map(int, input().split()))
p = list(map(int,input().split()))

r = 0
if s == t:
    r = 0
else:
    if s>t:
        r = n-1
    elif s<t:
        r = -1

print(r)