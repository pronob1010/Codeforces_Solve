# x = []
# for i in range(3):
#     x.append(int(input()))
#
# x.sort()
#
# if (2*x[0])+(2*x[1]) == (2*x[2]):
#     print("YES")
# else:
#     print("NO")

# s = input()
# x = s.count('0')
#
# r = min(x,len(s)-x)
# print(r)

# a = []
# x = []
# n = int(input())
# for i in range(n):
#     a = list(map(int, input().split()))
#     x.append(a)
# p = 0
# for i in range(n):
#     # print(x[i])
#     p += sum(x[i])
#
# ps = p//(n-1)
# # print(ps)
#
# x1 = []
# for i in range(n):
#     x1.append(ps-sum(x[i]))
#
# # print(x1)
#
# for i in range(n):
#     for j in x[i]:
#         if j is 0:
#             print(x1[i], end=" ")
#         else:
#             print(j, end=" ")
#     print()
#

n = int(input())
s = list(map(int , input().split()))
s.sort()
l= len(s)
if l<3:
    print(0)
else:
    c = 0
    for i in range(l):
        for j in range(i,l):
            if s[i]**2+s[j]**2==s[l-i]:
                c+=1
    print(c)
