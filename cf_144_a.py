n = int(input())
s = list(map(int, input().split()))[:n]
# print(s)
x = s.index(max(s))
s.remove(s[x])
s.reverse()
# print(s)
y = s.index(min(s))
print(x+y)

# m = max(s)
# mp = 0
# min = min(s)
# minp =0
# # print(m,min)
# if n == 2 or (s[0]==m and s[len(s)-1]==min):
#     if s[0]>s[len(s)-1]:
#         print('0')
#     else:
#         print('1')
# else:
#     for i in range(len(s)):
#         if s[i]>=m:
#             m = s[i]
#             mp = i
#
#     for i in range(len(s)):
#         if s[i]<=min:
#             min = s[i]
#             minp = i
#
#     # print(m, mp)
#     # print(min, minp)
#
#     if mp>minp:
#         minp+=1
#     # print(minp)
#     t = (mp+(len(s)-1)-minp)
#     print(t)
#

# n = int(input())
# s = list(map(int, input().split()))[:n]
# c = 0
# i=2
# m = max(s)
# min = min(s)
# while (not(s[0]==m and s[len(s)-1]==min)):
#     if (s[i-2] == min):
#         if  (s[i-2] < s[i-1]):
#             t = s[i-1]
#             s[i-1] = s[i-2]
#             s[i-2] = t
#             c += 1
#         if i<len(s):
#             i+=1
#         else:
#             i=2
#     if (s[i - 2] == min):
#         if (s[i - 2] > s[i - 1]):
#             t = s[i - 2]
#             s[i - 2] = s[i - 1]
#             s[i - 1] = t
#             c += 1
#         if i < len(s):
#             i += 1
#         else:
#             i = 2
#         print(s)
#     else:
#         if i < len(s):
#             i+=1
# print(c)

# s1={}
#
# for i in s:
#     if i in s1:
#         s1[i]+=1
#     else:
#         s1[i]=1
# x = []
# for i in s1.keys():
#     x.append(i)
#
# m = max(x)
# min = min(x)
# # print(x)
# mp = 0
# minp = 0
# for i in range(1,len(x)+1):
#     if x[i-1]==m:
#         mp=i
#         break
# for i in range(1,len(x)+1):
#     if x[i-1]==min:
#         minp = i
#         break
#
# # print(minp,mp)
# t = (mp-1)+(len(s)-minp)
# print(t)
# if t%2==0:
#     print(t)
# else:
#     print(t-1)
#


# # print(s[len(s)-1])
# # # c = 0
# # # i=2
# # # while (not(s[0]==m and s[len(s)-1]==min)):
# # #     if s[i-2] < s[i-1]:
# # #         t = s[i-2]
# # #         s[i-2] = s[i-1]
# # #         s[i-1] = t
# # #         c += 1
# # #     if i<len(s):
# # #         i+=1
# # #     else:
# # #
# # #         i=2
# # #     print(s)
# # # print(c)
