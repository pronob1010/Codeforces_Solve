s,n  = list(map(int, input().split()))
p = s
c = 0
f = 0
match = []
for i in range(n):
    x, y = list(map(int, input().split()))
    match.append([x,y])

match.sort()
# print(match)
for i in match:
    if i[0]>= p:
        print("NO")
        break
    else:
        p += i[1]
else:
    print("YES")