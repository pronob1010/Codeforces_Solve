# from sys import stdin
# input = lambda : stdin.readline()
#
# def gcd(a,b):
#     if b==0:
#         return a
#     else:
#         return gcd(b,a%b)
#
# while True:
#     n = int(input())
#     if n==0:
#         break
#     else:
#         g = 0
#         for i in range(1,n):
#             for j in range(i+1,n+1):
#                 # a= i
#                 # b =j
#                 # while(a!=b):
#                 #     if a>b:
#                 #         a-=b
#                 #     else:
#                 #         b-=a
#                 # g+=a
#                 a = max(i, j)
#                 b = min(i, j)
#                 g+= gcd(a,b)
#                 # print(g)
#         print(g)
#         g=0

