n = int(input())
s = list(map(int, input().split()))
s.sort()
r = 0
for i in range(len(s)):
    if i%2==0:
        r+= 3.141592653589*(s[i]**2)
    else:
        r-=3.141592653589*(s[i]**2)
if r<0:
    r = -1*r
print("%.10f"%r)
