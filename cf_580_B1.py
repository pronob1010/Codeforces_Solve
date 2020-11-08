# n, d = list(map(int, input().split()))
# li = []
# li2 = []
# for i in range(n):
#     m,s = list(map(int, input().split()))
#     li.append([m, s])
#
# li.sort(key = lambda li: li[1], reverse=True)
# c = 0
# # print(c)
# x = li[0][0]
# # print(x)
# j = 0
# r = 0
# for i in li:
#     if (i[0]-x)<d:
#         c+=i[1]
#         # print(li[j][0],c)
#
#
#     # r = max(r,c)
#             # print(abs(i[0] - x), i[1],c)
#     # print(i[0])
# print(r)
# print(li)
# #
n, d = list(map(int, input().split()))
li = []
for i in range(n):
    m,s = list(map(int, input().split()))
    li.append([m, s])

li.sort()
c = 0
# print(c)
x = li[0][0]
# print(x)
j = 0
r = 0
for i in li:
    c += i[1]
    while(i[0]-li[j][0])>=d:
            c-=li[j][1]
            j+=1
    # print(c)
    # print(c)
    r = max(r,c)
            # print(abs(i[0] - x), i[1],c)
    # print(i[0])
print(r)
print(li)
