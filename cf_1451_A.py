# import math
# x = int(input())
# for i in range(x):
#     n = int(input())
#
#     if n == 1:
#         print(0)
#     else:
#         c = 0
#         r = n
#         f = 0
#         while (r>1):
#             sq = math.ceil(math.sqrt(r))
#             # print(sq)
#             if r%sq==0:
#                 c+=1
#                 r = r/sq
#             else:
#                 r-=1
#                 c+=1
#         print(c)

x = int(input())
for i in range(x):
    n = int(input())
    r = 0
    while(n>1):
        if n%2==0:
            d = n//2
            n//=d
            r+=1
            if d==1:
                break

        elif n%2!=0:
            n-=1
            r+=1

        # print(n,r)


    print(r)