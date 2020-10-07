n,m = list(map(int,input().split()))
n1= list(map(int,input().split()))[:n]
c =0
for i in n1:
    ans = (c+i)//m
    c = (c+i)%m
    print(ans)
