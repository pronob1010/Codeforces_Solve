# t = int(input())
# for i in range(t):
#     n = int(input())
#     a = list(map(int, input().split()))[:n]
#     s = 0
#     b = []
#     b.append(a[0])
#     for i in range(2,n):
#         s = sum(b)
#
#         if s+a[i-1]!=0:
#             b.append(a[i-1])
#             a.remove(a[i-1])
#         else:
#             if sum(a)!=0:
#                 a.append(a[i-1])
#
#
#     print(*a, sep="  ")
#     print("----------")
#     print(b)
#     print("----------")
#
#
#
# # t = int(input())
# # for i in range(t):
# #     n = int(input())
# #     a = list(map(int, input().split()))[:n]
# #     b= []
# #
# #     i = 2
# #     c = []
# #     b.append(a[0])
# #     while(i<=n):
# #         x = sum(b)
# #         ns = x + a[i-1]
# #         if x != 0 and ns != 0:
# #             b.append(a[i - 1])
# #         else:
# #             c.append(a[i-1])
# #         i += 1
# #     j = 1
# #     while (len(c)!=0 and sum(c)!= 0):
# #         fc = sum(b)
# #         if c[j-1]+fc != 0:
# #             b.append(c[j-1])
# #             c.remove(c[j-1])
# #         else:
# #             c.append(c[j-1])
# #
# #     if sum(b) == 0:
# #         print("NO")
# #     else:
# #         print("YES")
# #         print(*b, sep=" ")
# #


t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))[:n]

    if sum(a)==0:
        print("NO")
    else:
        if sum(a)>0:
            a.sort(reverse=True)
            print("YES")
            print(*a,sep=" ")
        else:
            a.sort()
            print("YES")
            print(*a, sep=" ")
