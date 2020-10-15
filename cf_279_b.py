# n,t = list(map(int,input().split()))
# a = list(map(int,input().split()))[:n]
# c =0
# l=0
# for i in a:
#     if i<=t:
#         c+=1
#         t-=i
# print(c)
#

n,t = list(map(int,input().split()))
a = list(map(int,input().split()))[:n]
c =0
l=0
for i in range(n):
    l += a[i]
    if l>t:
        l-=a[c]
        c += 1
print(n-c)
