
n = {}
for i in range(int(input())):
    c = list(map(int,input().split()))
    evn = 0
    odd = 0
    m = min(c)
    for j in range(1,len(c)+1):
        c[j-1]-=m


    for k in range(1, len(c)+1):
        if c[k-1]%2==0:
            evn += 1
        elif c[k-1]%2==1:
            odd += 1
    if (odd == 1 or odd==0):
        print("Yes")
    else:
        print("No")




































    # # print(c)
    # mi = min(c)
    # if mi!=0:
    #     for i in range(1,len(c)-1):
    #         if c[i-1]>=mi:
    #             c[i-1]-=mi
    #             if c[i-1]%2==1:
    #                 o+=1
    #
    # if o==1:
    #     print("Yes")
    # else:
    #     print("No")

# o=0
# e=0
# for i in range(int(input())):
#     c = list(map(int,input().split()))
#     for j in range(1,len(c)+1):
#         if c[j-1]%2==1:
#             o=1
#         elif c[j-1]%2==0:
#             e+=1
#
#     print(o,e)
#     if e==len(c) or e==len(c)-1 and o<=1:
#         print("Yes")
#     else:
#         print("No")
#
#
#
# # f =0
# # for i in range(int(input())):
# #     c = list(map(int,input().split()))
# #     for j in range(2,len(c)+1):
# #         if c[j-2]==c[j-1]:
# #             f=1
# #         else:
# #             f==0
# #
# #     if f==0:
# #         for j in range(1,len(c)+1):
# #             if(c[j-1]==1 or c[j-1]%3==0 or c[j-1]%2==0 )and c[j-1]!=0:
# #                 f=1
# #             else:
# #                 f=0
# #                 break
# #
# #     if f == 1:
# #         print("Yes")
# #     else:
# #         print("No")