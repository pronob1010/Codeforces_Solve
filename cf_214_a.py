a,b = list(map(int,input().split()))
c1=0
c2=0

for i in range(a+1):
    for j in range(b+1):
        if ((i**2)+j)==b and ((j**2)+i) == a:
            # print("b",i, j)
            c1+=1
#
# for i in range(b):
#     for j in range(a):
#         if i**i+j == b:
#             c2+=1

print(c1)

