n = int(input())
s = list(map(int,input().split()))[:n]

c = 0

x = s[0]
x2 = s[0]

for i in range(1,n+1):
    if (s[i-1]>x):
        c+=1
        x = s[i-1]

    if (s[i - 1] < x2):
        c += 1
        x2 = s[i - 1]

print(c)

