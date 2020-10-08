t = int(input())
cashes = 1
time = []
for i in range(t):
    h = list(map(int, input().split()))
    time.append(h)
for j in range(len(time)):
    for k in range(len(time)):
        if j!=k and time[j]==time[k]:
            cashes+=1
            # print(j,k)
            # print(time[j])


print(cashes-(cashes//2))
