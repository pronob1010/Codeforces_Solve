t = int(input())
for i in range(t):
    n = int(input())

    j = 1
    r =0
    while (r<n):
        r+=j
        j+=1
    print(r,j)
    if r-1 == n:
        print(j)
    else:
        print(j-1)
