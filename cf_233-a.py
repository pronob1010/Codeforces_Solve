n = int(input())
if n%2==1:
    print('-1')
else:
    for i in range(n, 0, -1):
        print(i, end=" ")

# n = int(input())
# n1 = []
# f = 0
# if n==1:
#     print('-1')
# else:
#     for i in range(n,0,-1):
#         n1.append(i)
#
#     for i in range(0,len(n1)-1):
#         if i+1==n1[i]:
#             f =1
#             break
#
#     if f == 0:
#         print(*n1,sep=" ")
#     else:
#         print('-1')