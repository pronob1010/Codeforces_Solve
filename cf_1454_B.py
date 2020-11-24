# t = int(input())
# for i in range(t):
#     n = int(input())
#     s1 = list(map(int, input().split()))
#     s = s1
#     s1 = set(s1)
#     # print(len(s), len(s1))
#     if len(s)!=len(s1) and len(s1)==1:
#         print(-1)
#     else:
#         f = {}
#         for i in s:
#             if i in f:
#                 f[i]+=1
#             else:
#                 f[i]=1
#         # print(f.values())
#
#         if len(f.values())==len(s):
#             r = min(s)
#
#         elif len(f.values())==len(s):
#             se = set(f.values())
#             r = 0
#             if len(se)==1:
#                 r = -1
#
#         else:
#             r = min(f, key=f.get)
#
#         # print(r)
#         for i in range(len(s)):
#             if s[i]==r:
#                 print(i+1)
#                 break
#         else:
#             print(-1)

t = int(input())
for i in range(t):
    n = int(input())
    s1 = list(map(int, input().split()))
    f = {}
    for i in s1:
        if i in f:
            f[i]+=1
        else:
            f[i]=1
    # print(f)

    uni = []
    for key, value in f.items():
        if value ==1:
            uni.append(key)
    # print(uni)
    if len(uni)==0:
        print(-1)
    else:
        print(s1.index(min(uni))+1)