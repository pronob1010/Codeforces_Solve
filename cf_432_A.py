n, k = list(map(int, input().split()))
s = list(map(int, input().split()))

c = 0
list = []
for i in s:
    if i<=5-k:
        list.append(i)
# f={}
# for i in s:
#     if i in f:
#         f[i]+=1
#     else:
#         f[i]=1
# print(max(f.values()))
# max = max(f.values())
# if max<=k:
#     te=len(list)//3
#     if te<=k:
#         print(te)
# else:
#     print(0)
print(len(list)//3)
