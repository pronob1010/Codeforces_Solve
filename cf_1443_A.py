for i in range(int(input())):
    n = int(input())
    x = 4*n
    for j in range(n):
        x-=2
        print(x,end=" ")
    print()