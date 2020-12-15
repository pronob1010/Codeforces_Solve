
p = int(input())
for i in range(p):
    n = int(input())
    s=[]
    x=9
    if n>45 or n<0:
        print(-1)
    elif n==0:
        print(0)
    else:
        while n>0:
            if x<=n:
                s.append(x)
                n-=x
                x-=1
            else:
                x-=1
        s.sort()
        print(*s,sep="")
