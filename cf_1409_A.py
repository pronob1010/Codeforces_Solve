for i in range(int(input())):
    p,q = list(map(int, input().split()))
    c = 0
    a = min(p,q)
    b = max(p,q)
    while(a!=b):

        if abs(b-a)>=10:
            x = (abs(b-a)//10)
            b-=10*x
            c+=x
        else:
            b-=abs(b-a)
            c+=1

    print(c)