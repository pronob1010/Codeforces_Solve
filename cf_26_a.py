import math

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

n = 3000
p = []



n = int(input())
p= SieveOfEratosthenes(n)
# print(p)
z=0
for i in range(1,n+1):
    # x = int(math.sqrt(i))
    c= 0


    for j in range(1,len(p)+1):
        if i%p[j-1]==0:
            c+=1
    if c==2:
        z+=1


print(z)