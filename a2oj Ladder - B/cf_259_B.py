a = []
s1 =list(map(int,input().split()))
s2 =list(map(int,input().split()))
s3 =list(map(int,input().split()))

p = (sum(s1)+sum(s2)+ sum(s3))//2

x1 = p-sum(s1)
x2 = p-sum(s2)
x3 = p-sum(s3)

for i in range(3):
    if s1[i]==0:
        print(x1, end=" ")
    else:
        print(s1[i], end=" ")
print()
for i in range(3):
    if s2[i]==0:
        print(x2, end=" ")
    else:
        print(s2[i], end=" ")
print()
for i in range(3):
    if s3[i]==0:
        print(x3, end=" ")
    else:
        print(s3[i], end=" ")
print()