n = input()
i = len(n)-1
if n[0]=='1':
    # print(i)
    while i>=0:
        # print(n[i])
        if n[i]=='4' and n[i-1]=='4' and n[i-2]=='1':
            i-=3
            # print("fdfd")
        elif n[i]=='4' and n[i-1]=='1':
            i-=2
            # print("fd")
        elif n[i]=='1':
            # print("fdd")
            i-=1
        else:
            # print("ffd")
            break
    # print(i)
if i<0:
    print("YES")
else:
    print("NO")






















# n = input()
# f = 1
# i=0
# x =len(n)
# while(i<x):
#     if x>= 3:
#         if n[i] == '1' and n[i + 1] == '4' and n[i + 2] == '4':
#             i += 3
#     if x >= 2:
#         if n[i]=='1' and n[i+1] == '4':
#             i+=2
#     if x >= 1:
#         if n[i] == '1':
#             i += 1
#         else:
#             f = 0
#             break
#
# if f == 1:
#     print("YES")
# else:
#     print("NO")
#
#
# # li = []
# # nl1 = []
# # while(n!=0):
# #     li.append(n%10)
# #     n//=10
# # li.reverse()
# # f = 0
# # # nl1.append(li[0])
# # t = li[0]
# # if li[0] == 1:
# #     for i in range(1,len(li)-1):
# #         print(li[i])
# #         if li[i]!=t:
# #             t = li[i]
# #             f = 1
# #         elif t==1:
# #             continue
# #         else:
# #             f = 0
# #             break
# # else:
# #     f = 0
# #
# # if f == 1:
# #     print("YES")
# # else:
# #     print("NO")
#
#
#
# # f = 0
# # temp = []
# # temp.append(n % 10)
# # if (n != 1444) and (n != 514) and (n != 414):
# #     while n != 0:
# #         r = n % 10
# #         if (r == 1 or r == 4):
# #             if r== 4 and temp[len(temp)-1] ==r:
# #                 break
# #             f = 1
# #         else:
# #             f = 0
# #             break
# #         n = n // 10
# #
# #     if f == 1:
# #         print("YES")
# #     else:
# #         print("NO")
# # else:
# #     print("NO")
