t = int(input())
cashes = 0
time = []
for i in range(t):
    h = list(map(int, input().split()))
    time.append(h)


n = []

for j in range(len(time)):
    p = 0
    for k in range(len(time)):

        if j!=k and time[j]==time[k]:
            cashes+=1
            p += 1
            n.append(time[j])
            print(time[j])

print(p,len(n))
print(n)
print(time)
x = (cashes-(cashes//2))
if x <=1:
    print(x+1)
else:
    print(x)