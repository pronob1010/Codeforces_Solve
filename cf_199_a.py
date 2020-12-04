# def fibonacci(n):
#     flist = []
#     a = 0
#     b = 1
#     flist.append(a)
#     flist.append(b)
#
#     for i in range(2,n):
#         c = a + b
#         a = b
#         b = c
#         if b<n:
#             flist.append(b)
#         else:
#             flist.append(b)
#             break
#     return flist
#
# def twopinter(li,i,x):
#     z = 0
#     while i<=len(li):
#         if li[i]+li[len(li)-z]==x:
#             print(li[i], li[len(li)-z])
#             return li[i]+li[len(li)-z]
#         elif li[i]+li[len(li)-z] < x:
#             i+=1
#         elif li[i]+li[len(li)-z] > x:
#             z+=1
#         else:
#             return 0
#
#
# def threepointer(li,n):
#     st = 0
#     s = li[st]
#     while st<=len(li):
#         x = (n-s[st])
#         if s[st]+twopinter(li,st,x) == n:
#             print(s[st])
#             print("Done")
#         elif s[st]+twopinter(li,st,x) < n:
#             st+=1
#         else:
#             return False
#
#
#
#
#
#
#
# n = int(input())
# li = fibonacci(n)
# print(li)
#
# if threepointer(li,n) ==  False:
#     print("I'm too stupid to solve this problem")
# else:
#     print("")
#
#
#

n = int(input())
print(0, 0, n)