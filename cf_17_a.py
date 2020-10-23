def SieveOfEratosthenes(n):
   prime = [True for i in range(n + 1)]
   p = 2
   while (p * p <= n):
      if (prime[p] == True):
         for i in range(p * 2, n + 1, p):
            prime[i] = False
      p += 1

   prime[0]= False
   prime[1]= False

   pl = []
   for p in range(n + 1):
      if prime[p]:
         pl.append(p)
   return pl

n = 1000
p = []
x,y = list(map(int,input().split()))
p= SieveOfEratosthenes(x)
# print(p)
c =0
for i in range(len(p)-1):
    if p[i]+p[i+1]+1 in p:
        c+=1
# print(c)
if c >=y:
    print("YES")
else:
    print("NO")