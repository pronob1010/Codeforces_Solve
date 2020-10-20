n , l = list(map(int, input().split()))
a = list(map(int, input().split()))
a.sort()
# print(a)
m = 0

for i in range(2,len(a)+1):
    if abs((a[i-2]-a[i-1]))>m:
        # print(abs((a[i-2]-a[i-1])/2))
        m = abs((a[i-2]-a[i-1]))

x = a[0]
y = m/2
z = l-a[len(a)-1]
r = max(x,y,z)

print("%.10f"%r)