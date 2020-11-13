n , m = list(map(int, input().split()))
s = {}
for i in range(m):
    a,b = list(map(str, input().split()))
    if len(a)<=len(b):
        s[a]= a
    else:
        s[a]= b

s2 = list(map(str, input().split()))

for j in range(n):
    print(s[s2[j]], end=" ")
