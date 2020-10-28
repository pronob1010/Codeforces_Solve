import sys
input = sys.stdin.readline

q = int(input())
for _ in range(q):
    n, m = map(int, input().split())
    dictn = dict()

    for i in range(n):
        l = list(input().split())
        dictn[l[0]] = l

    for i in range(m):
        l = list(input().split())
        if l[0] in dictn:
            firstline = l

    for k in firstline:
        print(" ".join(dictn[k]))


# for i in range(int(input())):
#     n, m = list(map(int, input().split()))
#     m1 = []
#     for j in range(n):
#         s = list(map(int,input().split()))[:m]
#
#     for j in range(m):
#         l = list(map(int, input().split()))[:n]
#         m1.append(l)
#
#     # print(m1)
#
#     for z in range(n):
#         for i in range(len(m1)):
#             print(m1[i][(n-1)-((n-1)-z)],end=" ")
#         print()