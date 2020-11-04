a, b = list(map(int, input().split()))
a1 = list(map(int, input().split()))
b1 = list(map(int, input().split()))
v = min(a1)
bm = min(b1)

amin = max(a1)
# for i in b1:
#     if 2*i>2*v:
#         c+=1

if max(v*2,amin)<bm:
    print(max(v*2,amin))
else:
    print(-1)
# v = max(a1)
# bm = min(b1)
# # print(bm,v)
# c = 0
# if len(a1)>1:
#     for i in a1:
#         if 2*i<=v:
#             c+=1
# else:
#     c = 1
#
# d = 0
# for i in b1:
#     if i>v:
#         d+=1
#
# if len(a1)==1:
#     print(2*v)
# elif c>=1 and d == len(b1):
#     print(v)
# else:
#     print(-1)