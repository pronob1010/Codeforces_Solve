def gcd(a,b):
    if (b==0):
        return a
    else:
        return gcd(b,a%b)
n = int(input())
for i in range(n):
    x = int(input())
    c = []
    for i in range(2,4*x+1):
        a = i+1
        b = i
        if a%b!=0 and b%a!=0 or gcd(a,b)!=1:
            c.append(a)
            c.append(b)

    c = set(c)
    c2 = c
    # print(c)
    p = 0
    for l in c:
        for k in c2:
            if p<x:
                if l%k!=0:
                    p+=1
                    print(k, end=" ")
            else:
                break
    print()


#
# for i in range(int(input())):
#     a, b = list(map(int, input().split()))
#     s = input()
#     s.count()