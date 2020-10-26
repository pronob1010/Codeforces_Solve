for _ in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))[:n]
    s.sort()
    r = 1
    # print(s)
    c = 1
    for i in range(1, len(s)+1):
        # print(c)
        if c==5:
            if r > 0:
                r *= s[len(s) - 1]
                break
        else:
            r*=s[i-1]
        # print(r)
        c+=1

    print(r)