t = int(input())
c = 0
for i in range(t):
    tn, x = list(map(int,input().split()))
    for j in range(tn):
        n,m = list(map(int,input().split()))
        p,q = list(map(int,input().split()))

        if m==p:
            c=1

    if c==1 and x%2==0:
        print('YES')
    else:
        print('NO')
    c = 0
# 1
# # 1 100
# # 10 10
# # 10 10