n, m = list(map(int, input().split()))

r = n//m

c = 0
for i in range(0,r+1):

    for j in range(0,i):
        c += 1
print(c)