for _ in range(int(input())):
    n, m = list(map(int,input().split()))
    a1 = list(map(int,input().split()))[:n]
    b1 = list(map(int,input().split()))[:m]
    c=0
    cl=[]
    for i in range(len(b1)):
        if b1[i] in a1:
            print("YES")
            print(1, end=" ")
            print(b1[i])
            break
    else:
        print("NO")