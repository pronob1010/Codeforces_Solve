a,b = list(map(int,input().split()))
a = list(map(int, input().split()))

a.sort()
# print(a)
s = 0
for i in range(1,b+1):
    if a[i-1]<0:
        s += a[i-1]
    else:
        break
print(abs(s))


