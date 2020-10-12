import math
for _  in range(int(input())):
    x,y,n = list(map(int, input().split()))
    p = math.floor((n - y) / x)
    k = p*x + y
    print(k)

    # m = 0
    # o = n%x
    # if o<y:
    #     m = o+x-y
    #     print(n-m)
    # else:
    #     print(n-m+y)