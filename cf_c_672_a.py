t = int(input())
for j in range(t):
    n = int(input())
    nlist = list(map(int, input().split()))[:n]
    f = 0
    v = 10**10
    for i in range(n):
        if nlist[i] < v:
            v = nlist[i]
        else:
            f = 1


    if f == 1:
        print("YES")
    else:
        print("NO")



# t = int(input())
# for j in range(t):
#     n = int(input())
#     nlist = list(map(int, input().split()))[:n]
#
#     upper = 0
#     lower = 0
#     for i in range(1,n):
#         if nlist[i-1]<nlist[i]:
#             upper += 1
#         elif nlist[i-1]>nlist[i]:
#             lower += 1
#
#     print(lower,upper)
#     if upper==lower==0:
#         print("YES")
#     elif ((upper>lower and lower==0) or (upper<lower and upper==0)):
#         print("NO")
#     else:
#         print("YES")


    # print(upper,lower)







    # print(nlist)
    # for i in range(1,n):
    #     print(nlist[i-1],nlist[i])
    #     if int(nlist[i-1])<int(nlist[i]):
    #         # print("f",nlist[i])
    #         f +=1
    #     elif int(nlist[i-1])>int(nlist[i]):
    #         # print(" ", nlist[i])
    #         p +=1
    #
    #
    # print(f,p,i)
    # if f==0 and p==0:
    #     print("YES")
    # elif ((f==0) and (p>0)) or((f>0) and (p==0)):
    #     print("NO")
    # elif 0<f<n and 0<p<n:
    #     print("YES")
    #
    #
    # # if f<len(nlist) or f==0:
    # #     print("YES")
    # # else:
    # #     print("NO")







# # #
# # # def mergeSort(array):
# # #     if hasattr(mergeSort, "num"):
# # #         mergeSort.num += 1  # increment if not first call
# # #     else:
# # #         mergeSort.num = -1  # initialize on first call
# # #
# # #     if len(array) > 1:
# # #         r = len(array)//2
# # #         L = array[:r]
# # #         M = array[r:]
# # #
# # #         mergeSort(L)
# # #         mergeSort(M)
# # #
# # #         i = j = k = 0
# # #
# # #         while i < len(L) and j < len(M):
# # #             if L[i] < M[j]:
# # #                 array[k] = L[i]
# # #                 i += 1
# # #             else:
# # #                 array[k] = M[j]
# # #                 j += 1
# # #             k += 1
# # #
# # #         # When we run out of elements in either L or M,
# # #         # pick up the remaining elements and put in A[p..r]
# # #         while i < len(L):
# # #             array[k] = L[i]
# # #             i += 1
# # #             k += 1
# # #
# # #         while j < len(M):
# # #             array[k] = M[j]
# # #             j += 1
# # #             k += 1
# # #
# # #     return mergeSort.num
# # #
# # #
# # # lp = 0
# # # t = int(input())
# # # for j in range(t):
# # #     n = int(input())
# # #     turn = ((n*(n-1))/2)-1
# # #     nlist = list(map(int, input().split()))[:n]
# # #     p = 0
# # #     p = mergeSort(nlist)
# # #     lp = p-lp
# # #     if lp<=turn:
# # #         print('YES')
# # #     else:
# # #         print('NO')
# # #     print(p,turn)
# #
# # t = int(input())
# # for j in range(t):
# #     n = int(input())
# #     turn = ((n*(n-1))/2)-1
# #     nlist = list(map(int, input().split()))[:n]
# #     c = 0
# #     if turn>0:
# #         for passnum in range(len(nlist) - 1, 0, -1):
# #             for i in range(passnum):
# #                 if nlist[i] > nlist[i + 1]:
# #                     nlist[i], nlist[i+1] = nlist[i+1], nlist[i]
# #                     c += 1
# #         if c<turn:
# #             print('YES')
# #         else:
# #             print('NO')
# #     else:
# #         print('NO')
#
#
# t = int(input())
# for j in range(t):
#     n = int(input())
#     nlist = list(map(int, input().split()))[:n]
#     c = 0
#     for i in nlist:
#         for k in nlist:
#             if not(i==k):
#                 if i<k and ((i&k) > (i ^ k)):
#                         c +=1
#
#     if len(set(nlist)) == 1 and len(nlist)>1:
#         print(n)
#     else:
#         print(c)
#     c = 0
#
