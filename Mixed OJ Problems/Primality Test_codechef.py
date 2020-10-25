#https://www.codechef.com/problems/PRB01
for _ in range(int(input())):
    n = int(input())
    if n>1:
        i = 2
        f = 0
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
