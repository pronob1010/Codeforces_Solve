# https://www.spoj.com/problems/TDKPRIME/
def sieveOFerathenes(n):
    primebool= [True for i in range(n+1)]
    primebool[0]=False
    primebool[1]=False

    p = 2
    while(p*p<=n):
        if primebool[p]==True:
            for i in range(p*2,n+1,p):
                primebool[i]=False
        p+=1
    mainprime = []
    for i in range(2,n+1):
        if primebool[i-1] == True:
            mainprime.append(i-1)
    return mainprime
p = sieveOFerathenes(9000)
# print(p)
for _ in range(int(input())):
    n = int(input())
    print(p[n-1])
