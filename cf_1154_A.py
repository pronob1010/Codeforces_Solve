s = list(map(int, input().split()))
s.sort()
apb=s[0]
apc = s[1]
bpc = s[2]
apbpc = s[3]

c = apbpc - apb
b = bpc - c
a = apb-b
print(a,b,c)