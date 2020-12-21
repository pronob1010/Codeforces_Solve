t= int(input())
for i in range(t):
    s = int(input())
    while True:
        s1 = s
        while(s1>0):
            r = s1%10
            if(r != 0 and s%r != 0):
                break
            s1//=10

        if s1==0:
            print(s)
            break
        s+=1
