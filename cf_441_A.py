n, mp= list(map(int, input().split()))
r = []
for i in range(n):
    s1 = list(map(int, input().split()))
    s1_i =s1[0]
    s1_v = s1[1:]

    for j in range(s1_i):
        if s1_v[j]<mp:
            r.append(i+1)
if len(r)>0:
    r.sort()
    print(len(r))
    r = list(set(r))
    print(*r, sep=" ")
else:
    print(0)