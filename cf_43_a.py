n = int(input())
f = {}
for i in range(n):
    s = input()

    if s in f:
        f[s]+=1
    else:
        f[s]=1
# print(f)
print(max(f, key = f.get))
