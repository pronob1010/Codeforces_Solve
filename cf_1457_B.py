# #
# # t= int(input())
# # for i in range(t):
# #     n, k = list(map(int, input().split()))
# #     c = list(map(int, input().split()))
# #
# #     day = 0
# #     f = {}
# #     for i in c:
# #         if i in f:
# #             f[i]+=1
# #         else:
# #             f[i]=1
# #
# #     m = max(f, key=lambda x:f[x])
# #
# #
# #
# #
# #     # x = 0
# #     # for i in c:
# #     #     if i is not m:
# #     #         # print(i)
# #     #         if x<=k:
# #     #             x += 1
# #     #         else:
# #     #             x-=k
# #     #             if x % k:
# #     #                 day += 1
# #     #             x = 0
# #     #     else:
# #     #         print(x, day)
# #     #         if x>0:
# #     #             day+=1
# #     #         x = 0
# #     # print(day)
#
#
# from sys import stdin, stdout
# import math
#
# t = int(stdin.readline())
# for _ in range(t):
#     n, k = map(int, stdin.readline().split())
#     arr = list(map(int, stdin.readline().split()))
#     maxq = 0
#     col = {}
#     di = {}
#     for i in arr:
#         if i in di:
#             di[i] += 1
#         else:
#             di[i] = 1
#
#     mindays = 10 ** 9
#     for i in di:
#         start = 0
#         end = 0
#         days = 0
#         j = 0
#         while j < n:
#             if arr[j] == i:
#                 while j < n and arr[j] == i:
#                     j += 1
#             else:
#                 j += (k)
#                 days += 1
#         mindays = min(mindays, days)
#     print(mindays)
#
#
#
#
#
#

# import math
# t = int(input())
# for i in range(t):
#     n = input()
#
#     print(len(n))

t = int(input())
for i in range(t):
    n = int(input())

    x = 0
    j =0
    # while (x!=n):
    #     if x<n:
    #         x+=j
    #     elif x>n:
    #         x-=1
    #     j+=1

    while(x<n):
