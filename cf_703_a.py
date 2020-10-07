n = int(input())
m = 0
c = 0
for i in range(n):
    a,b = list(map(int,input().split()))
    if a>b:
        m+=1
    elif a<b:
        c+=1


if m==c:
    print("Friendship is magic!^^")
elif m>c:
    print("Mishka")
elif c>m:
    print("Chris")
m = 0
c = 0

