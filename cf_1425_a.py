n = int(input())
for j in range(10,n):
    if j%2==0:
        r = 0
        # n1 = int(input())
        n1 =j
        i=1
        while(n1!=0):
            if n1%2 == 0:
                if (i % 2 == 1):
                    r += n1//2
                n1 = n1//2
            elif n1%2 == 1:
                if (i % 2 == 1):
                    r += 1
                n1-=1
            i+=1
        print(j ,"-", r, end=", ")