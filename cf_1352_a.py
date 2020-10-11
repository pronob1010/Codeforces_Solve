t = int(input())
for i in range(t):
    s = input()
    l = len(s)
    ro = []
    mro = []
    for j in range(l,0,-1):
        if(int(s[j-1])>0):
            st = s[j-1]
            if (l-(j)) > 0:
                st+='0'*(l-(j))
            ro.append(st)
    print(len(ro))
    print(*ro, sep=" ")
