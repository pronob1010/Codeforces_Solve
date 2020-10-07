n = int(input())
l = []
c = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        # l.append( i*j)
        print(c+i, end=" ")

    c+=1
    print("\n")

# print(l)