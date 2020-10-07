t = int(input())
for i in range(t):
    n = int(input())
    j = 3
    p = 0
    while (p<n):
        p = ((j-2)*180)/j
        j+=1
    if p==n:
        print("YES")
    else:
        print("NO")