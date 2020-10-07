from collections import OrderedDict
n,m = list(map(int, input().split()))
winner = []
for i in range(m):
    s = list(map(int,input().split()))[:n]
    p = s[0]
    w=0
    for j in range(n):
        if s[j]>p:
            p= s[j]
            w = j
    winner.append(w+1)

fre = {}
fre1 = {}
for i in winner:
    if i in fre:
        fre[i] += 1
    else:
        fre[i] = 1
fre1=OrderedDict(sorted(fre.items()))

print(max(fre1, key=fre1.get))