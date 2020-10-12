import math
for _  in range(int(input())):
    x,y,n = list(map(int, input().split()))
    p = math.floor((n-y)/x)
    # m = 0
    # for i in range(n//2,n+1):
    #     o = i%x
    #     if o==y and o<=n and i>m:
    #         m = i

    k = p*x + y
    print(k)