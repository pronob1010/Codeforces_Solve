a, b = list(map(int, input().split()))
t = 240-b
s = 0
c = 0
for i in range(1,a+1):
    s += 5*i
    if s<=t:
        c+=1
    else:
        break

print(c)