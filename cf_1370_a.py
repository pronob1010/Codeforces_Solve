for _ in range(int(input())):
    n = int(input())
    m = 0
    for i in range(1,n):
        for j in range(1,n):
            if i>j:
                a=i
                b=j
                while b:
                    a,b = b,a%b

                if a>=m:
                    m = a
    print(m)
    m = 0