import math
t = int(input())
for i in range(t):
    n = int(input())
    r = math.sqrt(n)
    for j in range(2, int(r)):
        print(j)
        if n%j==0:
            r1 = j
            r2 = n-j
            print(r1, r2)
            break
