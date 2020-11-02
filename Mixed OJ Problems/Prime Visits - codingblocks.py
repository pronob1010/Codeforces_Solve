def SieveOfEratosthenes(n):
   prime = [True for i in range(n + 1)]
   prime[0] = False
   prime[1] = False
   p = 2
   countprime = []
   while (p * p <= n):
      if (prime[p] == True):
         for i in range(p * 2, n + 1, p):
             prime[i] = False
      p += 1
   for j in range(n+1):
       c = 0
       for i in range(j+1):
           if prime[i] == True:
               c += 1
       countprime.append(c)



   return countprime

n = 1000000
p = []
p = SieveOfEratosthenes(n)
# countprime = []
#
# print(p)
# for i in range(n):
#     c = 0
#     for j in range(i+1):
#         if p[j] == True:
#             c += 1
#     countprime.append(c)
#     # print(i,countprime[i])

for i in range(int(input())):
    a,b= list(map(int,input().split()))

    print(p[b-1]- p[a-1])