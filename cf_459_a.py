x1,y1,x2,y2 = list(map(int,input().split()))
l1 = abs(x1-x2)
l2 = abs(y1-y2)
if x1==x2:
    x3 = x1 + l2
    y3 = y1
    x4 = x2 + l2
    y4 = y2
elif y1==y2:
    x3 = x1
    y3 = y1 + l1
    x4 = x2
    y4 = y2 + l1
elif l1!=l2:
    print(-1)
else:
    x3 = x1
    y3 = y1
    x4 = x2
    y4 = y2
print(x3,y3,x4,y4)
