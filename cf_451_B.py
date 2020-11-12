n = int(input())
arr = list(map(int, input().split()))
xx  = sorted(arr)

if arr == xx:
    print('yes')
    print(1, 1)
else:
    start , end = 0, 0
    for i in range(0, n):
        if xx[i] != arr[i]:
            start = i
            break

    for j in range(n-1, -1, -1):
        if xx[j] != arr[j]:
            end = j
            break

    arr[start:end+1] = arr[start:end+1][::-1]
    if xx == arr:
        print('yes')
        print(start+1, end+1)
    else:
        print('no')





# x = int(input())
# n = list(map(int, input().split()))
#
# sort_n = sorted(n)
#
# if n == sort_n:
#     print("Yes")
#     print(sort_n[0],sort_n[0])
# else:
#     start =0
#     end = 0
#
#     for i in range(len(n)):
#         if n[i-1]>n[i]:
#             # print(i-1,i)
#             n[i-1],n[i] = n[i],n[i-1]
#             start = i-1
#             end = i
#             break
#     if sort_n == n:
#         print("yes")
#         print(sort_n[start],sort_n[end])
#     else:
#         print("no")
#
#
#
# # nc = n
# # nc.reverse()
# # start =0
# # end = 0
# # # print(nc)
# # for i in range(len(n)):
# #     if n[i-1]>n[i]:
# #         n[i-1],n[i] = n[i],n[i-1]
# #         start = i-1
# #         end = i
# #         break
# #
# # s = n
# # # print(s)
# # x = sorted(n)
# # # print(x)
# # if nc == x:
# #     # print(s)
# #     # print(n)
# #     print("yes")
# #     print(s[start], s[end])
# # elif s == x:
# #     print("yes")
# #     print(s[start], s[end])
# # else:
# #     print("no")