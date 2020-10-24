import math
for i in range(int(input())):
    n,m = list(map(int,input().split()))
    a = list(map(int,input().split()))[:n]
    s2 = sum(a)
    # print(m,s2)
    if m==int(s2):
        print("YES")
    else:
        print("NO")