t = int(input())
s = list(map(int, input().split()))[:t-1]
a,b = list(map(int, input().split()))
r =0
p = a-1
for i in range(a,b):
    r += s[p]
    p+=1

print(r)