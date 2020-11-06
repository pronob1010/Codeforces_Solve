for i in range(int(input())):
    n = int(input())
    c = 0
    while(n>1 and n%3==0):
        if n%6==0:
            n = n//6
        else:
            n*=2
        c += 1
    if n==1:
        print(c)
    elif n%6==0 or n%6!=3:
        print(-1)

    # print(c)

# if n>6:
    #     n=n-6
    #
    # while(n>0 and n!=1):
    #     # if n%6==3:
    #     #     c = (n//6)+2
    #     #     n = n%6
    #     # if n==3:
    #     #     n*=2
    #     #     c+=1
    #     # else:
    #     #     c = -1
    #     #     break
    #
    #     if n==2:
    #         c = -1
    #         break
    #     elif n==1:
    #         break
    #
    #     elif n<6:
    #         n*=2
    #         c+=1
    #         # print(n)
    #     elif n>=6:
    #         c+=n//6
    #         n=n%6
    #     # print(n)