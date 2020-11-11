# n = int(input())
# s = list(map(int, input().split()))
# f = {}
# for i in s:
#     if i in f:
#         f[i]+=1
#     else:
#         f[i]=1
# print(len(f))
#
# for i in f.items():
#     p = list(i)
#     if p[1]==1:
#         p[1]=0
#     print(*p , end=" ")
#     print()

n = int(input())
a = list(map(int, input().split()))
v = dict()

for i in range(n):
    x = a[i]
    if x in v:
        v[x] = [i, -1 if v[x][1] and i - v[x][0] != v[x][1] else i - v[x][0]]
    else:
        v[x] = (i, 0)

print(v)

b = [(x, v[x][1]) for x in sorted(v.keys()) if v[x][1] >= 0]
print(len(b))
for x, p in b: print(x, p)