# # # # # # n = int(input())
# # # # # # print(n**2)
# # # # # #
# # # # #
# # # # # a = int(input())
# # # # # b = int(input())
# # # # #
# # # # # print((a*b)*3)
# # # # r =0
# # # # for i in range(int(input())):
# # # #     r += int(input())*3
# # # #
# # # # print(r)
# # #
# # # r =0
# # # for i in range(int(input())):
# # #     n = int(input())
# # #     print(180*(n-2))
# #
# # n = int(input())
# # if n%3 == 0 and n%5==0:
# #     print("FizzBuzz")
# # elif n%3==0:
# #     print("Fizz")
# # elif n%5==0:
# #     print("Buzz")
#
# import math
# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
#
# r = math.sqrt((x2-x1)**2+(y2-y1)**2)
#
# print(r)

h = int(input())
m = int(input())
s = int(input())
s1 = input()

r = (((h*60)+m)*60)+s
print(r)