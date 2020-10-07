n = int(input())
s = list(map(int, input().split()))[:n]
me = 0
c = 0
s.sort()
r = sum(s)
for i in reversed(s):
    if r-me>= me:
        me+=i
        c += 1

print(c)