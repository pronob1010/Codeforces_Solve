a , b = list(map(int,input().split()))

odd = []
eve = []
r = []
for i in range(1,a+1):
    if i%2==0:
        eve.append(i)
    else:
        odd.append(i)

r = odd+eve
print(r[b-1])