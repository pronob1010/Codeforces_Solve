for i in range(int(input())):
    n,r = list(map(int, input().split()))
    s = list(map(int, input().split()))[:n]

    c = 0
    re = 0
    for j in s:
        if c<=r:
            re += j
            c += 1
    if re%2==1:
        print("Yes")
    else:
        print("No")


