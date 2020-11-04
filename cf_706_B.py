n = int(input())
x = list(map(int, input().split()))
x.sort()
q = int(input())
coin = []
for i in range(q):
    coin.append(int(input()))

for i in coin:
    c = 0
    for j in x:
        if i>= j:
            c+=1
    print(c)