import bisect
# def bs(s1,i,start):
#     r = start
#     start = 0
#     end = len(s1) - 1
#     while (start <= end):
#         mid = (start + (end - start) // 2)
#         # print(mid)
#         if s1[mid] <= i:
#             start = mid + 1
#             r = mid + 1
#         elif s1[mid] > i:
#             end = mid - 1
#
#     return r


n,m=list(map(int,input().split()))
s1 = list(map(int,input().split()))
s2 = list(map(int,input().split()))
s1.sort()
# s2.sort()
r = []
# r = 0
for i in s2:
    r.append(bisect.bisect(s1,i))
print(*r, end=" ")



# import bisect
# def bs(s1,i,start):
#     r = start
#     start = 0
#     end = len(s1) - 1
#     while (start <= end):
#         mid = (start + (end - start) // 2)
#         # print(mid)
#         if s1[mid] <= i:
#             start = mid + 1
#             r = mid + 1
#         elif s1[mid] > i:
#             end = mid - 1
#
#     return r
#
#
# n,m=list(map(int,input().split()))
# s1 = list(map(int,input().split()))
# s2 = list(map(int,input().split()))
# s1.sort()
# # s2.sort()
# # r = []
# r = 0
# for i in range(len(s2)):
#     r = bs(s1,s2[i],i)
#     # r.append(bisect.bisect(s1,i))
#     print(r, end=" ")
#
