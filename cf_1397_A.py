for i in range(int(input())):
    n = int(input())
    f = {}
    for j in range(n):
        s = input()
        for i in range(len(s)):
            if s[i] in f:
                f[s[i]]+=1
            else:
                f[s[i]]=1
    fl = 0
    # print(f)
    for k in f.values():
        if k>=n and k%n==0:
            fl=1
        else:
            fl=0
            break

    if (fl == 1):
        print("YES")
    else:
        print("NO")