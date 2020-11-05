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

    if (min(f.values())>=n):
        print("YES")
    else:
        print("NO")