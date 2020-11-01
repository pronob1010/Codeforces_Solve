

import math


# A function to print all prime factors of
# a given number n
def primeFactors(n,div):
    # Print the number of two's that divide n
    while n % 2 == 0:
        div.append(2)
        n = n //2

    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3, int(math.sqrt(n)) + 1, 2):

        # while i divides n , print i ad divide n
        while n % i == 0:
            div.append(i)
            n = n / i

        # Condition if n is a prime
    # number greater than 2
    if n > 2:
        div.append(n)

    # Driver Program to test above function




# This code is contributed by Harshit Agrawal


for i in range(int(input())):
    n, b = list(map(int, input().split()))
    if n>b:
        div = []
        div.append(1)
        div.append(n)
        primeFactors(n,div)
        div.sort(reverse=True)

        for i in range(len(n)):
            div.append(div[i-1]*div[len(div)-i])
        print(div)
    else:
        print(n)





