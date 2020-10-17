for i in range(int(input())):
    n = int(input())
    s = list(map(int,input().split()))[:n]
    c=0

    for j in range(1,n):
        if s[j-1]!=s[j]:
            c+=1;


    if c==0:
        print(n)
    else:
        print('1')