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

   return prime

n = 1000000
p = []
p= SieveOfEratosthenes(n)
for i in range(int(input())):
    a,b= list(map(int,input().split()))
    c = 0
    for i in range(a,b+1):
       if p[i]==True:
          c+=1
    print(c)
