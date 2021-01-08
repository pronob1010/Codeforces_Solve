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

#
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


# p = int(input())
# for l in range(p):
#     n = int(input())
#     s = list(map(int, input().split()))
#     s.sort()
#     c  = 0
#     s2 = s
#     s3 = 0
#     if len(set(s2)) == 1:
#         print(0)
#     else:
#         for i in range(1,len(s)):
#             s3 = (s[i-1]+s[i])
#             s3 = s[i+2:len(s)-1]
#             print(s3)
#

# p = int(input())
# for l in range(int(input())):
#     ss = int(input())
#     s = input()
#     g = 0
#     x = 0
#     f1 = 0
#     for i in range(len(s)-1,-1,-1):
#
#         if s[i]==')' and f1 == 0:
#             g+=1
#         else:
#             x += 1
#             f1 = 1
#
#     if g>x:
#         print("YES")
#     else:
#         print("NO")


# p = int(input())
# for l in range(int(input())):
#     ss =(input())
#
#     c = 0
#     while(True):
#         dig = []
#         if c == len(str(ss)):
#             print(ss-1)
#             break
#         else:
#             ss2 = ss
#             ss2 = str(ss2)
#             for i in range(len(str(ss))):
#                 if str(ss2[i]) != '0' and str(ss2[i]) not in dig:
#                     dig.append(int(ss2[i]))
#             for i in range(len(dig)):
#                 if int(ss)% dig[i] ==0:
#                     c +=1
#         ss = int(ss)+1

#
# xx= int(input())
# for l in range(xx):
#     x = int(input())
#     dig = x
#
#     while True:
#         s = str(dig)
#         result = dig
#         li  = []
#         c1=0
#
#
#         for i in s:
#
#             if i not in li and i!='0':
#                 li.append(i)
#
#         n_list = [int(k) for k in li]
#         lens = len(n_list)
#         for j in n_list:
#             if dig%j==0:
#                 c1+=1
#         if c1==lens:
#             break
#         else:
#             dig+=1
#     print(result)
#
#

# t = int(input())
# for i in range(t):
#     n, m= list(map(int, input().split()))
#     point = []
#     point_sel = []
#     for j in range(m):
#         s = list(map(int, input().split()))
#         point.append(s)
#     print(point)
#     for j in point:
#         if j[0] != j[1]:
#             point_sel.append(j)
#
#     print(point_sel)

# t = int(input())
# for i in range(t):
#     f = 0
#     r = 1
#     w, h, n = list(map(int, input().split()))
#
#     if w%2==0:
#         r += (w//2)*h
#     if h%2==0:
#         r += w*(h//2)
#
#     print(r)
#     if r >= n:
#          print("YES")
#     else:
#          print("NO")
import math
# t = int(input())
# for i in range(t):
#     n = int(input())
    # # x = 9
    # # print(x, end="")
    # # x = 9-(n-1)
    # last = (n//9)+ 9 - (n-1)
    # for j in range(1,n):
    #     pos = abs(n-j)
    #     x = last+pos
    #
    #     print(x, end="")
    # print(last)
    # r = n//9
    # x = 9
    # for j in range(r):
    #     print("9876543210",end="")
    # for k in range(n-(9*r)):
    #     print(x,end="")
    #     x-=1
    # print()
    # l = 8
    # n1 = ''
    # n2 = ''
    # loo = (n-1)//2
    # x = 9
    # x2 = 9
    # print(x,end="")
    # for j in range(loo):
    #     print(j)
    #
    # for j in range(n-loo):
    #     n2.join(x2)
    # # new = n1+reversed(n2)+l
    # print(n1,end="")
    # print(reversed(n2),end="")
    # print(l)
    # if n==1:
    #     print(9)
    # else:
    #     n-=1
    #     x = 8
    #     x2 = 0
    #     p1 = math.ceil(n/2)
    #     # print(p1)
    #     s = '9'
    #     for j in range(p1-1):
    #         if x2>9:
    #             x2 = 0
    #         pp = x2
    #         s+=str(pp)
    #         x2+=1
    #     print(s,end="")
    #     if n%2==0:
    #         s = reversed(s)
    #         print(*s,sep="",end="")
    #     else:
    #         print(s[len(s)-2:-1],end="")
    #     # print(s,end="")
    #     print(x)