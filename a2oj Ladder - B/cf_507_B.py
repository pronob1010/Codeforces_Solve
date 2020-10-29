r,x,y,x1,y1 = list(map(int, input().split()))

if x==x1 and y==y1:
    print(0)

elif x==x1:
    p = y1 // (r*2)
    if p<=r*2:
        print(1)
    else:
        print(p)
elif y==y1:
    p = x1 // (r*2)
    if p<=r*2:
        print(1)
    else:
        print(p)

else:
    a1 = abs(x-x1)
    a2 = abs(y-y1)

    if a1==a2:
        print(a1)
    else:
        print(min(a1,a2))