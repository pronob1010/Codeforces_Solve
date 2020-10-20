n,m,k = map(int, input().split(' '))
L = []
for i in range(m+1) :
    L.append(int(input()))
Fedor = L[len(L)-1]
del (L[len(L)-1])

# print(L)
# print(Fedor)

res = 0
for i in L :
    x = Fedor^i
    if bin(x).count('1') <= k:
        res +=1
print(res)
