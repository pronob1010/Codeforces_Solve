n = int(input())
r = 0
a1 = 0
b1= 0
c1= 0
for i in range(n):
    a,b,c = list(map(int, input().split()))
    # r += (a+b+c)
    a1 += a
    b1 += b
    c1 += c

if a1 is 0 and b1 is 0 and c1 is 0:
    print("YES")
else:
    print("NO")