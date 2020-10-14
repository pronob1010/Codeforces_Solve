t = int(input())
for j in range(t):
    n = int(input())
    nlist = list(map(int, input().split()))[:n]
    d = {}
    for i in range(n):
        print(bin(nlist[i]))
        k = len(bin(nlist[i]))

        if k in d:
            d[k]+=1
        else:
            d[k]=1

    ans = 0
    print(d)
    for i in d:
        print(d[i],d[i]-1)
        ans += (d[i]*(d[i]-1))//2
    print(ans)





# t = int(input())
# for j in range(t):
#     n = int(input())
#     nlist = list(map(int, input().split()))[:n]
#     c = 0
#     for i in nlist:
#         for k in nlist:
#             if not (i == k):
#                 if i < k and ((i & k) > (i ^ k)):
#                     c += 1
#
#     if len(set(nlist)) == 1 and len(nlist) > 1:
#         print(n)
#     else:
#         print(c)