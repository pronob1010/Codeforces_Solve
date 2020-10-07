n = int(input())
row = []
col = []

ans = 0
r = []
for i in range(n):
    col = list(map(int,input().split()))[:n]
    row.append(col)

for i in range(n):
    c = 0
    for j in range(n):
        if i==j:
            continue
        if row[i][j] == 0 or row[i][j]==2:
            c+=1
    if c == (n-1):
        ans += 1
        r.append(i+1)

print(len(r))
print(*r, sep=" ")