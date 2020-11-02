for i in range(int(input())):
    n1 = int(input())
    n = n1
    r7 = 0
    r5 = 0
    r3 = 0

    if n<3 or n==4:
        print(-1)
    else:
        if n%3==0:
            r3+=n//3

        elif (n-5)%3==0:
            r5 = 1
            r3+=(n-3)//3

        else:
            r3+=(n-7)//3
            r7 = 1


        print(r3, r5, r7)
