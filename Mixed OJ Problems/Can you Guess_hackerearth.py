p = int(input())
for i in range(p):
    n = int(input())
    r = 0
    j = 1
    while(j<n):
        if n%j==0:
            r+=j
        j+=1
    print(r)