for i in range(int(input())):
    n,r = list(map(int, input().split()))
    s = list(map(int, input().split()))[:n]

    c = 0
    re = s[0]
    if len(s) != r:
        for j in range(2,len(s)):

            if c<=r and ((re+s[j-1])%2==1):
                re += s[j-1]
                c += 1
    elif len(s) == r:
        re = sum(s)

    if re%2==1:
        print("Yes")
    else:
        print("No")


