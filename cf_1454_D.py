import math


# A function to print all prime factors of
# a given number n
def primeFactors(n):
    pp = []
    # Print the number of two's that divide n
    while n % 2 == 0:
        pp.append(2)
        n = n / 2

    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3, int(math.sqrt(n)) + 1, 2):

        # while i divides n , print i ad divide n
        while n % i == 0:
            pp.append(i)
            n = n / i

        # Condition if n is a prime
    # number greater than 2
    if n > 2:
        pp.append(n)
    return pp

t = int(input())
for i in range(t):
    n = int(input())
    ss= math.sqrt(n)
    x = 2
    f = 0
    while(x<=ss):
        if n%x==0:
            f = 1
        x+=1
    if f == 0:
        print(1)
        print(n)
    else:
        x = primeFactors(n)
        f = 0
        tt = 1
        print(x)

        fre = {}
        for i in range(len(x)):
            if x[i] in fre:
                fre[x[i]]+=1
            else:
                fre[x[i]] = 1

        m = max(fre, key=fre.get)
        mt= m
        times = fre.get(m)
        for i in range(len(x)):
            if x[i] != mt:
                mt*=x[i]
        print(times)
        for i in range(times-1):
            print(int(m), end=" ")
        print(int(mt))



        # for p in range(len(x)):
        #     tt *=  x[p]
        #     for i in range(len(x)):
        #         if tt%x[i]==0:
        #             f2 = 1
        #         else:
        #             f2 = 0
        #     if f2 == 1:
        #         w = p
        #         print(len(x[w+1:len(x)])+1)
        #
        #         rr = []
        #         for k in x[w+1:]:
        #             rr.append(k)
        #
        #         r1 = rr
        #         if (len(r1))>0:
        #             print(*r1,end=" ")
        #         print(int(tt))
        #         break
        # else:
        #     print(len(x))
        #     for i in x:
        #         print(int(i), end=" ")
        #     print()
