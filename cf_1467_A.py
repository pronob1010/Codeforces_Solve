
t = int(input())
for i in range(t):
    n = int(input())
    p1 = str(989)
    for j in range(3):
        if j<n:
            print(p1[j],end="")
    x = 0
    for j in range(n-3):   
        if x>9:
            x = 0
        print(x, end="")
        x+=1
    print()
