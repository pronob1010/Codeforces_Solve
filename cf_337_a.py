n,m=map(int,input().split())
a = list(map(int,input().split()))
a.sort()
min=a[n-1]-a[0]
i =0
# print(a)
# print(i + (n - 1), i, a[i + (n - 1)], a[i])

for i in range(1,len(a)-n+1):
    # print(i+(n-1),i,a[i+(n-1)],a[i])
    if (a[i+(n-1)]-a[i])<min:
        min=a[i+(n-1)]-a[i]

print(min)