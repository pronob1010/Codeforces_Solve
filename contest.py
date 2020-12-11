# # def gcd(a,b):
# #     if (b==0):
# #         return a
# #     else:
# #         return gcd(b,a%b)
# # n = int(input())
# # for i in range(n):
# #     x = int(input())
# #     c = []
# #     for i in range(2,4*x+1):
# #         a = i+1
# #         b = i
# #         if a%b!=0 and b%a!=0 or gcd(a,b)!=1:
# #             c.append(a)
# #             c.append(b)
# #
# #     c = set(c)
# #     c2 = c
# #     # print(c)
# #     p = 0
# #     for l in c:
# #         for k in c2:
# #             if p<x:
# #                 if l%k!=0:
# #                     p+=1
# #                     print(k, end=" ")
# #             else:
# #                 break
# #     print()
# #
# #
# # #
# # # for i in range(int(input())):
# # #     a, b = list(map(int, input().split()))
# # #     s = input()
# # #     s.count()
#
#
# # n = int(input())
# # for i in range(n):
# #     x = int(input())
# #     s = input()
# #     print(*sorted(s),sep="")
#
#
#
# # t = int(input())
# # # for i in range(t):
# # #     n, k = list(map(int, input().split()))
# # #     x = []
# # #     y = []
# # #     for j in range(n):
# # #         p = list(map(int, input().split()))
# # #         x.append(p[0])
# # #         y.append(p[1])
# # #
# # #     s = []
# # #     c = 0
# # #     for i in range(n):
# # #         for j in range(i + 1, n):
# # #             s.append(abs(x[i] - x[j]) + abs(y[i] - y[j]))
# # #
# # #     print(s)
# # #     if max(s)<=k:
# # #         print(1)
# # #     else:
# # #         print(-1)
#
# t = int(input())
# for i in range(t):
#     n, k = list(map(int, input().split()))
#     x = []
#     y = []
#     for j in range(n):
#         p = list(map(int, input().split()))
#         x.append(p[0])
#         y.append(p[1])
#
#     ll = len(x)
#     c = 0
#     f = 0
#     for i in range(ll):
#         c = 0
#         for j in range(ll):
#             if j == i:
#                 continue
#             else:
#                 s = abs(x[i] - x[j]) + abs(y[i] - y[j])
#                 if s <= k:
#                     c += 1
#                 else:
#                     break
#
#         if c==n-1 and f == 0:
#             f = 1
#             print(1)
#
#
#     if f == 0:
#         print(-1)
#
#
#







p = int(input())
for l in range(p):
    n , y = list(map(int, input().split()))
    s = ''.join([str('a') for i in range(y)])

    x = n-y
    a = 0
    b = 0
    c= 0
    for i in range(x):
        k = len(s)
        if s[k-1]!='c' and c==0:
            s = s+('c')
            c = 1
        elif s[k-1]!='b' and b==0:
            s = s+ ('b')
            b = 1
        elif s[k-1]!='a' and a==0:
            s = s+ ('a')
            b = 0
            c = 0
    print(s)


























