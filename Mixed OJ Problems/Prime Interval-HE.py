def seiveofErato(n):
    prime = [True for i in range(n+1)]
    prime[0]=False
    if n>0:
        prime[1]=False

    p = 2
    while(p*p<=n):
        if prime[p]==True:
            for i in range(p*2,n+1,p):
                prime[i]=False
        p+=1
    return prime

p = seiveofErato(10001)

a,b = list(map(int, input().split()))
for i in range(a,b+1):
    if p[i]==True:
        print(i, end=" ")
