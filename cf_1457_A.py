t= int(input())
for i in range(t):
    n, m, r, c = list(map(int, input().split()))

    a1 = (n-r)+(m-c)
    b2 = (abs(1-r)+abs(1-c))
    b3 = (abs(n-r)+abs(1-c))
    b4 = (abs(1-r)+abs(m-c))
    b5= (abs(n-r)+abs(m-c))

    r1 = max(a1,b2,b3,b4, b5)
    print(r1)
