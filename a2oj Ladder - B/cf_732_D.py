n, m = map(int, input().split(' '))
di = list(map(int,input().split(' ')))
ai = list(map(int,input().split(' ')))

completed = [False] * m
# print(completed)
sum = sum(ai) + m
temp = m

for i in range(n):
    if di[i] != 0:
        if not completed[di[i] - 1]:
            if ai[di[i] - 1] <= i:
                temp -= 1
                completed[di[i] - 1] = True

        if temp == 0:
            if i + 1 >= sum:
                print(i + 1)
                break
else:
    print(-1)
















# n , m = list(map(int , input().split()))
# d = list(map(int , input().split()))
# a = list(map(int , input().split()))
# a.sort(reverse=True)
# s = []
# temp = m
# sum = sum(a)+m
# for i in range(len(d)):
#     if d[i]!=0:
#         if len(s)!= m:
#             # print(d[i])
#             if d[i] not in s:
#                 if a[d[i]-1]<=i:
#                     s.append(d[i])
#                     temp -= 1
#     if temp==0:
#         if i+1 >= sum:
#             print(i + 1)
#             break
# else:
#     print(-1)