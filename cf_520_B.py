a,b = list(map(int, input().split()))
if a>b:
    print(a-b)
else:
    r = b%a
    if r==0:
        print(b//a)
    else:
        print(r)


# def solve(a, b, t):
#     t+=1
#
#     if a == b:
#         return True
#
#     elif a>b:
#         return False
#
#     elif a<=2:
#         return False
#
#     else:
#         if solve(a-1, b, t):
#             return t
#         else:
#             t -=1
#
#         if solve(a*2, b, t):
#             return t
#         else:
#             t -=1
#
#
#
# a,b = list(map(int, input().split()))
# t = 0
# if a>b:
#     print(a-b)
# else:
#     c = solve(a, b, t)
#     print(c)
#
# # import math
# # a,b = list(map(int, input().split()))
# #
# # c = 0
# # while True:
# #     if a>math.ceil(b/2) and a!=b:
# #         a-=1
# #         c+=1
# #     else:
# #         if a!=b:
# #             c += 1
# #             a*=2
# #         else:
# #             break
# # print(c)