# # # def gcd(a,b):
# # #     if (b==0):
# # #         return a
# # #     else:
# # #         return gcd(b,a%b)
# # # n = int(input())
# # # for i in range(n):
# # #     x = int(input())
# # #     c = []
# # #     for i in range(2,4*x+1):
# # #         a = i+1
# # #         b = i
# # #         if a%b!=0 and b%a!=0 or gcd(a,b)!=1:
# # #             c.append(a)
# # #             c.append(b)
# # #
# # #     c = set(c)
# # #     c2 = c
# # #     # print(c)
# # #     p = 0
# # #     for l in c:
# # #         for k in c2:
# # #             if p<x:
# # #                 if l%k!=0:
# # #                     p+=1
# # #                     print(k, end=" ")
# # #             else:
# # #                 break
# # #     print()
# # #
# # #
# # # #
# # # # for i in range(int(input())):
# # # #     a, b = list(map(int, input().split()))
# # # #     s = input()
# # # #     s.count()
# #
# #
# # # n = int(input())
# # # for i in range(n):
# # #     x = int(input())
# # #     s = input()
# # #     print(*sorted(s),sep="")
# #
# #
# #
# # # t = int(input())
# # # # for i in range(t):
# # # #     n, k = list(map(int, input().split()))
# # # #     x = []
# # # #     y = []
# # # #     for j in range(n):
# # # #         p = list(map(int, input().split()))
# # # #         x.append(p[0])
# # # #         y.append(p[1])
# # # #
# # # #     s = []
# # # #     c = 0
# # # #     for i in range(n):
# # # #         for j in range(i + 1, n):
# # # #             s.append(abs(x[i] - x[j]) + abs(y[i] - y[j]))
# # # #
# # # #     print(s)
# # # #     if max(s)<=k:
# # # #         print(1)
# # # #     else:
# # # #         print(-1)
# #
# # t = int(input())
# # for i in range(t):
# #     n, k = list(map(int, input().split()))
# #     x = []
# #     y = []
# #     for j in range(n):
# #         p = list(map(int, input().split()))
# #         x.append(p[0])
# #         y.append(p[1])
# #
# #     ll = len(x)
# #     c = 0
# #     f = 0
# #     for i in range(ll):
# #         c = 0
# #         for j in range(ll):
# #             if j == i:
# #                 continue
# #             else:
# #                 s = abs(x[i] - x[j]) + abs(y[i] - y[j])
# #                 if s <= k:
# #                     c += 1
# #                 else:
# #                     break
# #
# #         if c==n-1 and f == 0:
# #             f = 1
# #             print(1)
# #
# #
# #     if f == 0:
# #         print(-1)
# #
# #
# #
#
#
#
#
#
# #
# #
# # p = int(input())
# # for l in range(p):
# #     n , y = list(map(int, input().split()))
# #     s = ''.join([str('a') for i in range(y)])
# #
# #     x = n-y
# #     a = 0
# #     b = 0
# #     c= 0
# #     for i in range(x):
# #         k = len(s)
# #         if s[k-1]!='c' and c==0:
# #             s = s+('c')
# #             c = 1
# #         elif s[k-1]!='b' and b==0:
# #             s = s+ ('b')
# #             b = 1
# #         elif s[k-1]!='a' and a==0:
# #             s = s+ ('a')
# #             b = 0
# #             c = 0
# #     print(s)
# #
# #
# #
#
# p = int(input())
# for l in range(p):
#     arr = []
#     n,m = list(map(int, input().split()))
#     for i in range(n):
#         s = input()
#         x = s.count('*')
#         arr.append(x)
#     r = sum(arr)
#     print(arr)
#     for i in range(1,len(arr)):
#         if arr[i-1]<=arr[i]:
#             r+=arr[i-1]
#         if arr[i-1]>arr[i] and arr[i]>2:
#             r+=arr[i]-1
#
#     print(r)
#
#
#


#
# p = int(input())
# for l in range(p):
#     n = int(input())
#     s = list(map(int, input().split()))
#     s2 = []
#     j = 0
#     for i in range(len(s)):
#         p = s[i]
#         q = s[len(s)-1-i]
#         s2.append(p)
#         s2.append(q)
#
#     for i in range(len(s2)//2):
#         print(s2[i],end=" ")
#     print()
#
# p = int(input())
# for l in range(p):
#     n = int(input())
#     s = input()
#     s2 = []
#     c  = 0
#
#     j = 0
#     if s[j]=='2' and s[j+1]=='0' and s[j+2]=='2' and s[j+3]=='0':
#         print("YES")
#     elif s[j] == '2' and s[j + 1] == '0' and s[j+2] == '2' and s[n - 1] == '0':
#         print("YES")
#     elif s[j]=='2' and s[j+1]=='0' and s[n-2]=='2' and s[n-1]=='0':
#         print("YES")
#
#     elif s[j]=='2' and s[n-3]=='0' and s[n-2]=='2' and s[n-1]=='0':
#         print("YES")
#     elif s[n-4]=='2' and s[n-3]=='0' and s[n-2]=='2' and s[n-1]=='0':
#         print("YES")
#
#     else:
#         print("NO")
# p = int(input())
# for i in range(p):
#     n = int(input())
#     s=[]
#     x=9
#     if n>45 or n<0:
#         print(-1)
#     elif n==0:
#         print(0)
#     else:
#         while n>0:
#             if x<=n:
#                 s.append(x)
#                 n-=x
#                 x-=1
#             else:
#                 x-=1
#         s.sort()
#         print(*s,sep="")
p = int(input())
for l in range(p):
    n = int(input())
    s = list(map(int, input().split()))
    s.sort()
    c  = 0
    s2 = s
    s3 = 0
    if len(set(s2)) == 1:
        print(0)
    else:
        for i in range(1,len(s)):
            s3 = (s[i-1]+s[i])
            s3 = s[i+2:len(s)-1]
            print(s3)

