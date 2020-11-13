n , k = list(map(int, input().split()))
s = list(map(int, input().split()))

mc = 0
for i in range(n):
    f = {}
    c = 0
    t = str(s[i])
    # print(len(t))
    for j in range(len(t)):

        if t[j]=='4' or t[j]=='7':
            c+=1
    # print(c)

    if c>=0 and c <=k:
        mc+=1
print(mc)