import math
for i in range(int(input())):
    n1 = int(input())
    s = list(map(int, input().split()))[:2*n1]
    n = []
    for j in range(2,len(s)+1):
        print(math.gcd(s[j-1], s[j-2]))
        if math.gcd(s[j-1], s[j-2])>1:

            if len(n)<=(n1-1):
                n.append(s[j-1]+s[j-2])

    print(n)