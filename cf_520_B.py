x, y = list(map(int, input().split()))
a = min(x,y)
b = max(x,y)
c = 0
while(a<=b):
    if a!= b:
        if a*2<=b and ((a*2)-1)==a:

        if a*2<=b:
            c+=1
            a = a*2
        else:
            a-=1
            c+=1
    else:
        break
print(c)