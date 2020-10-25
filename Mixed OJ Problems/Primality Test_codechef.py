#https://www.codechef.com/problems/PRB01
t = int(input())
for j in range(t):
    n = int(input())
    f = 0
    if n>1:
        i = 2
        while(i*i<=n):
            if n%i==0:
                print("no")
                f = 1
                break
            i+=1
        if f == 0:
            print("yes")
    else:
        print("no")
