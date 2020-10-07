n = int(input())
li = list(map(int, input().split()))[:n]
r_li = []

for i in range(1,len(li)):
    if i%2 == 1:
        sum = li[i] + li[i-1]
    else:
        sum = li[i-1] + li[i]

    r_li.append(sum)

r_li.append(li[len(li)-1])
print(*r_li, sep=" ")