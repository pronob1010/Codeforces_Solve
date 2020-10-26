n=int(input())
k=2*n
l=2
for i in range(2*n+1):
    if(i<=n):
        for j in range(k):
            print(" ",end="")
        j=0
        while(j<2*i):
            if(j<=i):
                print(j,"",end="")
                m=j
            else:
                m-=1
                print(m,"",end="")
            j+=1
        print("0")
        k-=2
    else:
        for j in range(l):
            print(" ",end="")
        r=n-(i-n)
        j=0
        while(j<2*r):
            if(j<=r):
                print(j,"",end="")
                m=j
            else:
                m-=1
                print(m,"",end="")
            j+=1
        print("0")
        l+=2





